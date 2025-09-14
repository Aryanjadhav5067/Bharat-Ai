from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    prompt = f"You are Bharat AI, an expert in astrology, finance, daily life, science, technology, and history.
User: {user_input}
Bharat AI:"

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
