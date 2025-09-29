from flask import Flask, request, jsonify
from message_generator import generate_message

app = Flask(__name__)

@app.route('/generate-message', methods=['POST'])
def create_message():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    message = generate_message(prompt)
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
