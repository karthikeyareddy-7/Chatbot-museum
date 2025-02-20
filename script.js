document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value.trim();
    
    if (userInput) {
        addMessage(userInput, 'user-message');
        document.getElementById('user-input').value = '';

        // Send user input to the backend
        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            addMessage(data.response, 'bot-message');
        })
        .catch(error => {
            addMessage("I'm having trouble processing your request. Please try again later.", 'bot-message');
        });
    }
});

function addMessage(message, className) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('p');
    messageElement.className = `message ${className}`;
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
