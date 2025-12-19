const chatFeed = document.getElementById('chat-feed');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const uploadBtn = document.getElementById('upload-btn');
const imageInput = document.getElementById('image-input');
const micBtn = document.getElementById('mic-btn');
const timeBadge = document.getElementById('time-badge');

let selectedImage = null;

// Clock
setInterval(() => {
    const now = new Date();
    timeBadge.querySelector('span').textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}, 1000);

// Auto-expand textarea
userInput.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});

// Image Upload
uploadBtn.addEventListener('click', () => imageInput.click());
imageInput.addEventListener('change', (e) => {
    if (e.target.files && e.target.files[0]) {
        selectedImage = e.target.files[0];
        // Visual feedback
        uploadBtn.style.color = '#7b2cbf';
        userInput.placeholder = `Image selected: ${selectedImage.name}`;
    }
});

// Mic Logic (Simple placeholder or Web Speech API)
micBtn.addEventListener('click', () => {
    // Check browser support
    if ('webkitSpeechRecognition' in window) {
        micBtn.style.color = 'red'; // Recording state
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onresult = function (event) {
            userInput.value = event.results[0][0].transcript;
            micBtn.style.color = ''; // Reset
            userInput.focus();
        };

        recognition.onerror = function () {
            micBtn.style.color = '';
        };

        recognition.start();

    } else {
        alert("Speech recognition not supported in this browser context.");
    }
});

// Send Message
async function sendMessage() {
    const text = userInput.value.trim();
    if (!text && !selectedImage) return;

    // Add User Message to UI
    appendMessage(text, 'user', selectedImage);

    // Clear Input
    userInput.value = '';
    userInput.style.height = 'auto';
    userInput.placeholder = "Ask me anything...";
    uploadBtn.style.color = ''; // Reset upload icon

    // Store image ref processing
    const imageToSend = selectedImage;
    selectedImage = null; // Clear immediately for next

    // Send to Backend
    const formData = new FormData();
    if (text) formData.append('message', text);
    if (imageToSend) formData.append('image', imageToSend);

    try {
        // Show Loading/Typing...
        const loaderId = showTypingIndicator();

        const response = await fetch('/api/chat', {
            method: 'POST',
            body: formData
        });

        removeMessage(loaderId);

        if (!response.ok) throw new Error("Network error");

        const data = await response.json();
        appendMessage(data.response, 'system');

    } catch (err) {
        console.error(err);
        appendMessage("I am having trouble connecting. Please try again.", 'system');
    }
}

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

function appendMessage(text, type, imageFile = null) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${type}-message`;

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.innerHTML = type === 'system'
        ? '<ion-icon name="boat"></ion-icon>'
        : '<ion-icon name="person"></ion-icon>';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';

    let contentHtml = '';
    if (imageFile) {
        contentHtml += `<div style="margin-bottom:10px; color:#ccc; font-size:0.8rem;">[Sent an Image]</div>`;
    }
    if (text) {
        contentHtml += text.replace(/\n/g, '<br>');
    }
    bubble.innerHTML = contentHtml;

    msgDiv.appendChild(avatar);
    msgDiv.appendChild(bubble); // Order depends on flex-direction in CSS, but DOM order matters for logic sometimes. 
    // CSS handles reordering for user-message via flex-direction: row-reverse. so we can keep append order consistent.

    chatFeed.appendChild(msgDiv);
    chatFeed.scrollTop = chatFeed.scrollHeight;

    return msgDiv;
}

function showTypingIndicator() {
    const id = 'loader-' + Date.now();
    const msgDiv = document.createElement('div');
    msgDiv.className = `message system-message`;
    msgDiv.id = id;

    msgDiv.innerHTML = `
        <div class="avatar"><ion-icon name="boat"></ion-icon></div>
        <div class="bubble" style="color: #aaa; font-style: italic;">Processing...</div>
    `;
    chatFeed.appendChild(msgDiv);
    chatFeed.scrollTop = chatFeed.scrollHeight;
    return id;
}

function removeMessage(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
}
