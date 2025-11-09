from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialize OpenAI client (only if API key is set)
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key) if api_key else None

@app.route('/')
def index():
    """Main page of ContaX website"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/services')
def services():
    """Services page"""
    return render_template('services.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    API endpoint for LLM chat functionality
    Accepts a message and returns an AI-generated response
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Check if API key is configured
        if not client or not os.getenv('OPENAI_API_KEY'):
            return jsonify({
                'response': 'Olá! Sou o assistente virtual da ContaX. Como posso ajudá-lo hoje? (Modo demo - configure a API key para respostas personalizadas)'
            })
        
        # Create chat completion with OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente virtual da ContaX, uma empresa de contabilidade. Seja prestativo, profissional e forneça informações sobre serviços contábeis, fiscais e financeiros. Responda em português."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        return jsonify({'response': ai_response})
    
    except Exception as e:
        app.logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': 'Ocorreu um erro ao processar sua mensagem. Tente novamente.'}), 500

if __name__ == '__main__':
    # Only enable debug mode if explicitly set in environment
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
