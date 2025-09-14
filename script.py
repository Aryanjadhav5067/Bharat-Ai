import zipfile
import os

# Create directories and files for backend
os.makedirs('BharatAiApp/backend', exist_ok=True)

# Create app.py
app_py = '''from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    prompt = f"You are Bharat AI, an expert in astrology, finance, daily life, science, technology, and history.\nUser: {user_input}\nBharat AI:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7,
        n=1
    )

    answer = response.choices[0].text.strip()
    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(debug=True)
'''

with open('BharatAiApp/backend/app.py', 'w') as f:
    f.write(app_py)


# Create requirements.txt
requirements_txt = '''flask
flask-cors
openai
gunicorn
'''
with open('BharatAiApp/backend/requirements.txt', 'w') as f:
    f.write(requirements_txt)


# Create frontend files
os.makedirs('BharatAiApp/frontend', exist_ok=True)

# index.html
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Bharat AI Chatbot</title>
<link rel="stylesheet" href="styles.css" />
</head>
<body>

<div class="chat-container" role="main" aria-label="Bharat AI chatbot interface">
  <header class="header">Bharat AI Chatbot</header>
  
  <section class="messages" id="messages" aria-live="polite" aria-relevant="additions">
    <!-- Messages will appear here -->
  </section>
  
  <form class="input-container" id="chat-form" aria-label="Send message form">
    <input id="chat-input" type="text" autocomplete="off" placeholder="Ask Bharat AI..." aria-label="Chat input" required />
    <button type="submit" aria-label="Send message">Send</button>
  </form>
</div>

<script src="app.js"></script>

</body>
</html>
'''
with open('BharatAiApp/frontend/index.html', 'w') as f:
    f.write(index_html)

# styles.css
styles_css = '''/* Reset and basic styles */
* {
  box-sizing: border-box;
}
body {
  margin: 0;
  background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

/* Chat container */
.chat-container {
  width: 400px;
  max-width: 100%;
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 12px 24px rgb(37 117 252 / 0.4);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  animation: slideUp 0.5s ease forwards;
}

@keyframes slideUp {
  from {
    transform: translateY(50px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Header */
.header {
  background: #2575fc;
  color: white;
  padding: 20px;
  font-size: 1.5em;
  font-weight: 700;
  text-align: center;
  letter-spacing: 1.5px;
}

/* Chat messages container */
.messages {
  flex-grow: 1;
  padding: 16px;
  overflow-y: auto;
  background: #f6faff;
}

/* Message bubbles */
.message {
  max-width: 75%;
  padding: 12px 16px;
  margin-bottom: 12px;
  border-radius: 20px;
  opacity: 0;
  animation: fadeInUp 0.4s ease forwards;
  position: relative;
  font-size: 1rem;
  line-height: 1.3;
  word-wrap: break-word;
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
  from {
    opacity: 0;
    transform: translateY(20px);
  }
}

.message.user {
  background: #2575fc;
  color: white;
  margin-left: auto;
  border-bottom-right-radius: 4px;
}

.message.bot {
  background: #eaefff;
  color: #222;
  border-bottom-left-radius: 4px;
}

/* Input container */
.input-container {
  display: flex;
  padding: 12px 16px;
  background: white;
  border-top: 1px solid #ddd;
  align-items: center;
}

/* Input field */
.input-container input[type="text"] {
  flex-grow: 1;
  padding: 14px 16px;
  font-size: 1rem;
  border: 2px solid #2575fc;
  border-radius: 30px;
  outline: none;
  transition: border-color 0.3s ease;
}

.input-container input[type="text"]:focus {
  border-color: #6a11cb;
}

/* Send button */
.input-container button {
  background: #2575fc;
  border: none;
  color: white;
  padding: 14px 20px;
  margin-left: 12px;
  border-radius: 30px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 6px 12px rgb(37 117 252 / 0.3);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.input-container button:hover {
  background: #6a11cb;
  transform: scale(1.05);
}

.input-container button:active {
  transform: scale(0.95);
}
'''
with open('BharatAiApp/frontend/styles.css', 'w') as f:
    f.write(styles_css)

# app.js
app_js = '''const messagesEl = document.getElementById("messages");
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");

// Append a message to chat window
function appendMessage(text, sender) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);
  messageDiv.textContent = text;
  messagesEl.appendChild(messageDiv);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

// Disable input while waiting response
function setInputEnabled(enabled) {
  chatInput.disabled = !enabled;
  chatForm.querySelector("button").disabled = !enabled;
}

async function sendMessage(userMessage) {
  appendMessage(userMessage, "user");
  setInputEnabled(false);

  try {
    const response = await fetch("https://YOUR_BACKEND_URL/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage }),
    });

    if (!response.ok) throw new Error("Server error");

    const data = await response.json();
    appendMessage(data.response, "bot");
  } catch (error) {
    appendMessage("Sorry, something went wrong. Please try again.", "bot");
  }

  setInputEnabled(true);
  chatInput.focus();
}

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const message = chatInput.value.trim();
  if (!message) return;
  chatInput.value = "";
  sendMessage(message);
});
'''
with open('BharatAiApp/frontend/app.js', 'w') as f:
    f.write(app_js)


# Create zip
zipf = zipfile.ZipFile('BharatAiApp.zip', 'w', zipfile.ZIP_DEFLATED)

for foldername, subfolders, filenames in os.walk('BharatAiApp'):
    for filename in filenames:
        filePath = os.path.join(foldername, filename)
        zipf.write(filePath, os.path.relpath(filePath, 'BharatAiApp'))

zipf.close()

'BharatAiApp.zip'