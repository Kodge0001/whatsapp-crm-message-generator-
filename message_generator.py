import openai

# Replace with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_message(prompt):
    """
    Generates a predefined WhatsApp message based on user prompt.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a short, polite WhatsApp message for this scenario: {prompt}",
        max_tokens=60,
        temperature=0.7
    )
    return response.choices[0].text.strip()
