const messagesEl = document.getElementById("messages");
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
