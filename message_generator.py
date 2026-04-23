import os
import random
from dotenv import load_dotenv

load_dotenv()

# Template-based messages (works without any API key)
TEMPLATES = {
    "greeting": [
        "Hi {name}! 👋 Hope you're doing well. Just wanted to check in!",
        "Hello {name}! 😊 How's everything going on your end?",
        "Hey {name}! 🌟 Great to connect with you today!",
    ],
    "follow_up": [
        "Hi {name}! Just following up on our last conversation. Would love to hear your thoughts! 🙏",
        "Hey {name}! Hope you had a chance to look into what we discussed. Let me know if you have questions! 😊",
        "Hello {name}! Checking in — any updates on your end? Looking forward to hearing from you! ✨",
    ],
    "thank_you": [
        "Hi {name}! Just wanted to say a big THANK YOU for your support! 🙏❤️ Really appreciate it!",
        "Hey {name}! Thanks so much for everything — you're amazing! 🌟",
        "Hello {name}! Grateful for your help — it means the world! Thank you! 😊🙏",
    ],
    "promotion": [
        "Hi {name}! 🎉 Exciting news! We have a special offer just for you. Check it out!",
        "Hey {name}! 🔥 Don't miss our latest deal — limited time only! Let me know if you're interested!",
        "Hello {name}! ✨ We've got something special coming your way. Stay tuned!",
    ],
    "appointment": [
        "Hi {name}! 📅 Just a reminder about our upcoming meeting. Looking forward to it!",
        "Hey {name}! ⏰ Friendly reminder — we're scheduled to connect soon. See you there!",
        "Hello {name}! 📋 Confirming our appointment. Please let me know if the timing still works!",
    ],
    "general": [
        "Hi {name}! 👋 {message}",
        "Hey {name}! 😊 {message}",
        "Hello {name}! 🌟 {message}",
    ],
}


def detect_category(prompt):
    """Detect message category from the prompt."""
    prompt_lower = prompt.lower()
    if any(w in prompt_lower for w in ["greet", "hello", "hi", "welcome"]):
        return "greeting"
    elif any(w in prompt_lower for w in ["follow", "check in", "update"]):
        return "follow_up"
    elif any(w in prompt_lower for w in ["thank", "appreciate", "grateful"]):
        return "thank_you"
    elif any(w in prompt_lower for w in ["promo", "offer", "deal", "discount", "sale"]):
        return "promotion"
    elif any(w in prompt_lower for w in ["appoint", "meeting", "schedule", "remind"]):
        return "appointment"
    return "general"


def generate_message(prompt, name="there"):
    """
    Generate a WhatsApp message. Uses OpenAI if API key is set,
    otherwise falls back to templates.
    """
    api_key = os.getenv("OPENAI_API_KEY", "")

    # Try OpenAI if key is available and valid
    if api_key and api_key != "your_openai_api_key_here":
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes short, polite WhatsApp messages for business CRM. Keep messages under 50 words, friendly and professional."},
                    {"role": "user", "content": f"Write a WhatsApp message for: {prompt}. Address the person as {name}."}
                ],
                max_tokens=80,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI error (falling back to templates): {e}")

    # Template-based fallback
    category = detect_category(prompt)
    templates = TEMPLATES.get(category, TEMPLATES["general"])
    template = random.choice(templates)
    return template.format(name=name, message=prompt)
