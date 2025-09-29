# WhatsApp CRM Message Generator

A simple Flask-based service to generate predefined WhatsApp messages using prompts.

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Set your OpenAI API key in message_generator.py

3. Run the app:
   python app.py

4. POST to /generate-message with JSON:
   {
       "prompt": "I want to send a Diwali wish to my customers"
   }

5. Response:
   {
       "message": "Hello {name}, Diwali greetings! Wishing you joy, prosperity, and happiness this festive season. Namaste!"
   }
