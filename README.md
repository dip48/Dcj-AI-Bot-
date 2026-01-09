# 🤖 DCJ AI Telegram Bot


A simple **Telegram chatbot** built with Python that uses the **Groq API** for AI responses and stores chat data locally in JSON format.

---

## 📂 Project Structure

```
Chatbot/
│
├─ run.py          # Main entry point
├─ run.bat         # Windows launcher
├─ Chatbot.py      # Core bot logic
│
└─ data/
   └─ ChatLot.json # Chat history / data storage

README.md
.env               # Environment variables (NOT pushed to GitHub)
.env.example       # Sample environment file
```

---

## ⚙️ Requirements

* Python **3.9+** (recommended 3.10 or 3.11)
* Telegram Bot Token
* Groq API Key

Install dependencies:

```bash
pip install -r requirements.txt
```

*(If you don’t have `requirements.txt`, install manually: `python-telegram-bot`, `groq`, `python-dotenv`)*

---

## 🔐 Environment Variables

⚠️ **IMPORTANT:** Never upload your real `.env` file to GitHub.

Create a file named **`.env`** in the project root.

### `.env.example`

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
BOT_TOKEN=your_telegram_bot_token_here

GROQ_API_KEY=your_groq_api_key_here
GroqAPIkey=your_groq_api_key_here

Username=your_username
Assistantname=Dcj ai bot
```

Copy it and rename to `.env`, then fill in your real values.

---

## ▶️ How to Run

### Option 1: Run with Python

```bash
python run.py
```

### Option 2: Run on Windows (BAT file)

```bat
run.bat
```

---

## 🧠 Features

* Telegram chatbot integration
* AI responses powered by **Groq LLM**
* Local chat storage using JSON (`ChatLot.json`)
* Simple and lightweight structure

---

## 🚀 Deployment Tips

* Use **Railway**, **Render**, or **VPS** for 24/7 uptime
* Store secrets as environment variables on the server
* Disable debug logs in production

---

## 🔒 Security Notice

If you have **already exposed your API keys publicly**, you should:

1. **Revoke/Rotate** your Telegram Bot Token
2. **Regenerate** your Groq API Key
3. Update your `.env` file

---

## 👤 Author

**Dip**
Telegram AI Project – *Dcj AI Bot*

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🛠️ Improve it

Happy coding! 🚀


python-telegram-bot==22.5
python-dotenv==1.2.1
groq==1.0.0
rich==14.2.0
