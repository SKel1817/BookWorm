from flask import Flask, request
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.traceback import install
from rich.panel import Panel

load_dotenv()
install()  # Enable Rich traceback
console = Console()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
        GOOGLE_GEMINI_API_KEY=os.getenv('GOOGLE_GEMINI_API_KEY', ''),
    )

    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Log startup message - Flask 3 compatible way (using app_context)
    with app.app_context():
        console.log("[bold green]✅ BookWorm application ready to serve requests![/bold green]")

    @app.before_request
    def before_request():
        if request.endpoint not in ['static', 'json_version']:  # Skip logging for static file requests and /json/version
            console.log(Panel(
                f"[bold]Path:[/bold] {request.path}\n[bold]Method:[/bold] {request.method}", 
                title="[cyan]📥 Request[/cyan]", 
                border_style="cyan",
                expand=False
            ))

    @app.after_request
    def after_request(response):
        if request.endpoint not in ['static', 'json_version']:  # Skip logging for static file requests and /json/version
            console.log(Panel(
                f"[bold]Status:[/bold] {response.status}",
                title="[magenta]📤 Response[/magenta]",
                border_style="magenta",
                expand=False
            ))
        return response

    @app.teardown_request
    def teardown_request(exception):
        if exception:
            console.log(Panel(
                f"[bold]Exception:[/bold] {str(exception)}",
                title="[red]❌ Error[/red]",
                border_style="red",
                expand=False
            ))
        
    return app