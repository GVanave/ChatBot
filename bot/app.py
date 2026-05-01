"""
Simple AI Chatbot Backend — Flask + OpenAI API
Run: python app.py
"""

import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static")
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# In-memory conversation history (per session)
conversations = {}

SYSTEM_PROMPT = """You are a helpful, friendly, and concise AI assistant. 
Answer questions clearly and accurately. If you don't know something, say so honestly."""


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    print(data)

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    session_id = data.get("session_id", "default")
    user_message = data["message"].strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Initialize conversation history for new sessions
    if session_id not in conversations:
        conversations[session_id] = []

    # Add user message to history
    conversations[session_id].append({
        "role": "user",
        "content": user_message
    })

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT}
            ] + conversations[session_id],
            max_tokens=1024,
            temperature=0.7,
        )

        assistant_reply = response.choices[0].message.content

        # Save assistant reply to history
        conversations[session_id].append({
            "role": "assistant",
            "content": assistant_reply
        })

        return jsonify({
            "reply": assistant_reply,
            "session_id": session_id
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/reset", methods=["POST"])
def reset():
    data = request.get_json()
    session_id = data.get("session_id", "default")
    conversations.pop(session_id, None)
    return jsonify({"status": "reset", "session_id": session_id})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    print(f"🚀 Chatbot running at http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=debug)
