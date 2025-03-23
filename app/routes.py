from flask import Blueprint, render_template, request, jsonify, send_from_directory, redirect, url_for, flash, session
import requests
from bs4 import BeautifulSoup
import json
import os
import re
from app.gemini import gemini_ai

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/reader')
def reader():
    url = request.args.get('url')
    if not url:
        return render_template('index.html', error="Please provide a URL")
    
    try:
        # Add http:// if missing from the URL
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        # Fetch the content from the URL
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else "Untitled"
        
        # Clean up title
        title = re.sub(r'\s+', ' ', title).strip()
        
        # Extract main content - more sophisticated approach
        content = extract_main_content(soup)
        
        return render_template('reader.html', title=title, content=content, url=url)
    
    except Exception as e:
        return render_template('index.html', error=f"Error processing URL: {str(e)}")

def extract_main_content(soup):
    """Extract the main content from the webpage using a more sophisticated approach"""
    # Remove unwanted elements
    for element in soup.find_all(['script', 'style', 'nav', 'header', 'footer', 'aside']):
        element.extract()
    
    # Try to find the main content container
    main_content = None
    
    # Look for common content container elements with highest priority
    content_containers = soup.find_all(['article', 'main', '[role="main"]', '.content', '#content', '.post', '.entry'])
    
    if content_containers:
        # Choose the container with the most paragraphs
        main_content = max(content_containers, key=lambda x: len(x.find_all('p')))
    else:
        # If no obvious container, try to find a div with the most paragraphs
        divs = soup.find_all('div')
        if divs:
            main_content = max(divs, key=lambda x: len(x.find_all('p')))
    
    # If still no content found, use the body
    if not main_content or len(main_content.find_all('p')) < 2:
        main_content = soup.body
    
    # Format content for display in the reader
    formatted_content = ""
    
    # Extract and format headings and paragraphs
    if main_content:
        # Add the title as an h1 if it exists and we don't already have one
        if soup.title and not main_content.find('h1'):
            formatted_content += f"<h1>{soup.title.string.strip()}</h1>"
            
        # Process paragraphs and headings
        for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img', 'ul', 'ol', 'blockquote']):
            # Skip empty paragraphs
            if element.name == 'p' and (not element.text.strip() or len(element.text.strip()) < 10):
                continue
                
            # Handle images
            if element.name == 'img' and element.get('src'):
                img_src = element['src']
                # Convert relative URLs to absolute
                if img_src.startswith('/'):
                    img_src = '//' + soup.get('domain', '') + img_src
                formatted_content += f'<img src="{img_src}" alt="{element.get("alt", "")}" />'
                continue
                
            # Add the element as-is
            formatted_content += str(element)
    
    # If we couldn't extract meaningful content, provide a fallback message
    if not formatted_content or len(formatted_content) < 100:
        formatted_content = "<p>Sorry, we couldn't extract meaningful content from this page. You can view the original source instead.</p>"
    
    return formatted_content

@main_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        secret_key = request.form.get('secret_key')
        if secret_key != os.getenv('SECRET_KEY'):
            flash('Invalid secret key', 'error')
            return redirect(url_for('main.settings'))
        
        session['secret_key_verified'] = True
        google_gemini_key = request.form.get('google_gemini_key') or ''
        enable_gemini = 'enable_gemini' in request.form
        gemini_model = request.form.get('gemini_model') or 'gemini-1.0-pro'
        flask_port = request.form.get('flask_port') or '8080'
        
        # Update .env file
        with open(os.path.join(os.path.dirname(__file__), '../.env'), 'r') as file:
            lines = file.readlines()
        with open(os.path.join(os.path.dirname(__file__), '../.env'), 'w') as file:
            for line in lines:
                if line.startswith('GOOGLE_GEMINI_API_KEY='):
                    file.write(f'GOOGLE_GEMINI_API_KEY={google_gemini_key}\n')
                elif line.startswith('ENABLE_GEMINI_API='):
                    file.write(f'ENABLE_GEMINI_API={"true" if enable_gemini else "false"}\n')
                elif line.startswith('GEMINI_MODEL='):
                    file.write(f'GEMINI_MODEL={gemini_model}\n')
                elif line.startswith('FLASK_RUN_PORT='):
                    file.write(f'FLASK_RUN_PORT={flask_port}\n')
                else:
                    file.write(line)
        
        # Re-initialize Gemini AI with new settings
        os.environ['GOOGLE_GEMINI_API_KEY'] = google_gemini_key
        os.environ['ENABLE_GEMINI_API'] = 'true' if enable_gemini else 'false'
        os.environ['GEMINI_MODEL'] = gemini_model
        gemini_ai._initialize()
        
        flash('Settings updated successfully', 'success')
        return redirect(url_for('main.settings'))
    
    if not session.get('secret_key_verified'):
        return render_template('settings.html', secret_key_verified=False)
    
    google_gemini_key = os.getenv('GOOGLE_GEMINI_API_KEY', '')
    enable_gemini = os.getenv('ENABLE_GEMINI_API', 'false').lower() == 'true'
    gemini_model = os.getenv('GEMINI_MODEL', 'gemini-1.0-pro')
    flask_port = os.getenv('FLASK_RUN_PORT', '8080')
    return render_template('settings.html', 
                           secret_key_verified=True, 
                           google_gemini_key=google_gemini_key, 
                           enable_gemini=enable_gemini,
                           gemini_model=gemini_model,
                           flask_port=flask_port, 
                           secret_key=session.get('secret_key'))

@main_bp.route('/json/version')
def json_version():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'params.json')) as config_file:
            config = json.load(config_file)
            version = config.get('VERSION', 'unknown')
            return jsonify({'version': version})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(main_bp.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@main_bp.route('/api/chat', methods=['POST'])
def api_chat():
    """
    Process messages through the Gemini API and return the response
    
    Required POST parameters:
    - message: The user's message to process
    
    Optional POST parameters:
    - context: Additional context to send to the model
    """
    if not gemini_ai.is_available():
        return jsonify({
            'success': False, 
            'error': 'Gemini API is not enabled or properly configured'
        }), 503
    
    message = request.json.get('message')
    context = request.json.get('context')
    
    if not message:
        return jsonify({
            'success': False,
            'error': 'Message parameter is required'
        }), 400
    
    # Process the message with Gemini
    response = gemini_ai.generate_response(message, context)
    return jsonify(response)

@main_bp.route('/api/chat/status', methods=['GET'])
def api_chat_status():
    """Return the current status of the Gemini API integration"""
    return jsonify({
        'enabled': gemini_ai.enabled,
        'initialized': gemini_ai.initialized,
        'available': gemini_ai.is_available(),
        'model': gemini_ai.model
    })