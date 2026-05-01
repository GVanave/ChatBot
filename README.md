# 🤖 Simple AI Chatbot — OpenAI + Flask

A clean chatbot using OpenAI's GPT-3.5-turbo with a beautiful dark-themed frontend.

---

## 📁 Project Structure

```
chatbot/
├── app.py              # Flask backend (OpenAI API)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── README.md           # This file
└── static/
    └── index.html      # Frontend UI
```

---

## ⚡ Quick Start

### 1. Clone / download this project

### 2. Create your `.env` file
```bash
cp .env.example .env
```
Open `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-key-here
```
> Get your key at: https://platform.openai.com/api-keys

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
python app.py
```

### 5. Open the chatbot
Visit: **http://localhost:5000**

---

## 🔧 Configuration

| Variable        | Default         | Description              |
|-----------------|-----------------|--------------------------|
| OPENAI_API_KEY  | *(required)*    | Your OpenAI API key      |
| PORT            | 5000            | Flask server port        |
| FLASK_DEBUG     | false           | Enable debug mode        |

---

## 💡 Features

- 💬 Multi-turn conversation with memory
- 🔄 Reset conversation button
- ⌨️ Typing indicator
- 📱 Responsive design
- 🌙 Dark theme UI
- ⚡ Enter to send, Shift+Enter for newline

---

## 🔌 API Endpoints

| Method | Endpoint    | Description              |
|--------|-------------|--------------------------|
| GET    | `/`         | Serve the frontend       |
| POST   | `/api/chat` | Send a message           |
| POST   | `/api/reset`| Clear conversation       |

### POST `/api/chat`
```json
// Request
{ "message": "Hello!", "session_id": "optional-id" }

// Response
{ "reply": "Hi! How can I help?", "session_id": "..." }
```
