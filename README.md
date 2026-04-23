# WhatsApp CRM Message Generator 💬

A Flask-based web app that generates professional WhatsApp messages for CRM use.

## Features
- 🎯 **Smart category detection** — auto-detects greeting, follow-up, thank you, promotion, or appointment
- 📋 **One-click copy** — copy generated messages to clipboard
- 🤖 **Optional AI** — uses OpenAI GPT if an API key is provided, otherwise uses built-in templates
- 🌐 **Web UI** — clean, dark-themed interface

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open [http://localhost:5052](http://localhost:5052) in your browser.

## Optional: Enable AI-powered messages

1. Copy `.env.example` to `.env`
2. Add your OpenAI API key
3. Restart the app

```bash
cp .env.example .env
# Edit .env and add your key
```

## Tech Stack
- Python / Flask
- OpenAI API (optional)
- Vanilla HTML/CSS/JS frontend
