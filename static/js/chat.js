// Chat functionality for ContaX LLM integration

document.addEventListener('DOMContentLoaded', function() {
    const chatInput = document.getElementById('chatInput');
    const sendButton = document.getElementById('sendButton');
    const chatMessages = document.getElementById('chatMessages');

    if (!chatInput || !sendButton || !chatMessages) {
        console.error('Chat elements not found');
        return;
    }

    // Send message function
    async function sendMessage() {
        const message = chatInput.value.trim();
        
        if (!message) {
            return;
        }

        // Add user message to chat
        addMessage(message, 'user');
        chatInput.value = '';

        // Show typing indicator
        const typingDiv = addTypingIndicator();

        try {
            // Send message to API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            // Remove typing indicator
            typingDiv.remove();

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            if (data.error) {
                addMessage('Desculpe, ocorreu um erro. Por favor, tente novamente.', 'bot');
            } else {
                addMessage(data.response, 'bot');
            }
        } catch (error) {
            typingDiv.remove();
            console.error('Error:', error);
            addMessage('Desculpe, não foi possível processar sua mensagem. Verifique sua conexão e tente novamente.', 'bot');
        }
    }

    // Add message to chat
    function addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const messageParagraph = document.createElement('p');
        messageParagraph.textContent = text;
        messageDiv.appendChild(messageParagraph);
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        return messageDiv;
    }

    // Add typing indicator
    function addTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-indicator';
        typingDiv.innerHTML = '<p>Digitando...</p>';
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        return typingDiv;
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    console.log('Chat functionality initialized');
});
