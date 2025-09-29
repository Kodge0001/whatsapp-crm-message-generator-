import openai

# Replace with your OpenAI API key
openai.api_key = "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"

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
