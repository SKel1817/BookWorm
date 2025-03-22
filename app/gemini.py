import os
import google.generativeai as genai
from typing import Optional, Dict, Any
import logging

class GeminiAI:
    """
    Wrapper class for the Google Gemini API.
    This handles API initialization and message processing.
    """
    def __init__(self):
        self.api_key = os.environ.get('GOOGLE_GEMINI_API_KEY')
        self.enabled = os.environ.get('ENABLE_GEMINI_API', 'false').lower() == 'true'
        self.model = os.environ.get('GEMINI_MODEL', 'gemini-1.0-pro')
        self.initialized = False
        self.logger = logging.getLogger(__name__)
        
        # Try to initialize the API if enabled and key is provided
        self._initialize()
    
    def _initialize(self) -> bool:
        """
        Initialize the Gemini API with the provided API key.
        Returns True if initialization was successful, False otherwise.
        """
        if not self.enabled:
            self.logger.info("Gemini API is disabled via configuration.")
            return False
        
        if not self.api_key or self.api_key.lower() == 'none':
            self.logger.warning("Gemini API key not configured. Chat functionality will be disabled.")
            return False
        
        try:
            genai.configure(api_key=self.api_key)
            self.initialized = True
            self.logger.info(f"Gemini API initialized successfully with model {self.model}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to initialize Gemini API: {str(e)}")
            return False
    
    def is_available(self) -> bool:
        """Check if the Gemini API is available and properly initialized."""
        return self.enabled and self.initialized
    
    def generate_response(self, message: str, context: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate a response using the Gemini API for the given message and optional context.
        
        Args:
            message: The user's message to process
            context: Optional context to provide to the model
        
        Returns:
            A dictionary with 'success' and either 'response' or 'error' keys
        """
        if not self.is_available():
            return {
                'success': False,
                'error': 'Gemini API is not available or properly configured'
            }
            
        try:
            # Create full prompt with context if provided
            prompt = message
            if context:
                prompt = f"Context: {context}\n\nQuestion: {message}"
            
            # Generate response from Gemini
            model = genai.GenerativeModel(self.model)
            response = model.generate_content(prompt)
            
            # Return successful response
            return {
                'success': True,
                'response': response.text
            }
        except Exception as e:
            self.logger.error(f"Error generating response from Gemini: {str(e)}")
            return {
                'success': False,
                'error': f"Error: {str(e)}"
            }

# Create a singleton instance
gemini_ai = GeminiAI()