from flask import Flask, request, jsonify, render_template_string
from message_generator import generate_message

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp CRM Message Generator</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #0a0f1a; color: #e0e0e0; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .container { max-width: 520px; width: 100%; padding: 40px; background: rgba(20,30,50,0.9); border-radius: 20px; border: 1px solid rgba(37,211,102,0.2); box-shadow: 0 8px 40px rgba(0,0,0,0.4); }
        h1 { text-align: center; margin-bottom: 8px; font-size: 1.6rem; color: #25d366; }
        .subtitle { text-align: center; color: #888; margin-bottom: 28px; font-size: 0.9rem; }
        label { display: block; margin-bottom: 6px; font-weight: 600; font-size: 0.9rem; color: #aaa; }
        input, textarea, select { width: 100%; padding: 12px 16px; margin-bottom: 16px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; color: #fff; font-size: 0.95rem; outline: none; transition: border 0.3s; }
        input:focus, textarea:focus, select:focus { border-color: #25d366; }
        textarea { min-height: 80px; resize: vertical; }
        select { cursor: pointer; }
        select option { background: #1a2540; }
        button { width: 100%; padding: 14px; background: linear-gradient(135deg, #25d366, #128c7e); color: #fff; border: none; border-radius: 12px; font-size: 1rem; font-weight: 700; cursor: pointer; transition: all 0.3s; }
        button:hover { transform: translateY(-2px); box-shadow: 0 4px 20px rgba(37,211,102,0.4); }
        button:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }
        .result { margin-top: 20px; padding: 20px; background: rgba(37,211,102,0.08); border: 1px solid rgba(37,211,102,0.2); border-radius: 12px; display: none; }
        .result h3 { color: #25d366; margin-bottom: 10px; font-size: 0.95rem; }
        .result p { line-height: 1.6; font-size: 0.95rem; white-space: pre-wrap; }
        .copy-btn { margin-top: 12px; padding: 8px 16px; background: rgba(37,211,102,0.15); border: 1px solid rgba(37,211,102,0.3); border-radius: 8px; color: #25d366; cursor: pointer; font-size: 0.85rem; width: auto; }
        .copy-btn:hover { background: rgba(37,211,102,0.25); }
        .error { color: #ff6b6b; background: rgba(255,107,107,0.1); border-color: rgba(255,107,107,0.3); }
    </style>
</head>
<body>
    <div class="container">
        <h1>💬 WhatsApp CRM</h1>
        <p class="subtitle">Generate professional WhatsApp messages instantly</p>

        <label for="name">Recipient Name</label>
        <input type="text" id="name" placeholder="e.g., Rahul" value="there">

        <label for="category">Message Category</label>
        <select id="category">
            <option value="">Auto-detect from prompt</option>
            <option value="greeting">👋 Greeting</option>
            <option value="follow_up">🔄 Follow Up</option>
            <option value="thank_you">🙏 Thank You</option>
            <option value="promotion">🎉 Promotion</option>
            <option value="appointment">📅 Appointment</option>
        </select>

        <label for="prompt">What's the message about?</label>
        <textarea id="prompt" placeholder="e.g., Follow up with client about project proposal"></textarea>

        <button id="generateBtn" onclick="generateMessage()">✨ Generate Message</button>

        <div class="result" id="result">
            <h3>📝 Generated Message:</h3>
            <p id="messageOutput"></p>
            <button class="copy-btn" onclick="copyMessage()">📋 Copy to Clipboard</button>
        </div>
    </div>

    <script>
        async function generateMessage() {
            const btn = document.getElementById('generateBtn');
            const result = document.getElementById('result');
            const output = document.getElementById('messageOutput');
            const prompt = document.getElementById('prompt').value.trim();
            const name = document.getElementById('name').value.trim() || 'there';

            if (!prompt) { alert('Please enter a message prompt!'); return; }

            btn.textContent = 'Generating...';
            btn.disabled = true;

            try {
                const res = await fetch('/generate-message', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt, name })
                });
                const data = await res.json();

                if (data.error) {
                    output.textContent = data.error;
                    result.classList.add('error');
                } else {
                    output.textContent = data.message;
                    result.classList.remove('error');
                }
                result.style.display = 'block';
            } catch (err) {
                output.textContent = 'Failed to generate. Please try again.';
                result.classList.add('error');
                result.style.display = 'block';
            }

            btn.textContent = '✨ Generate Message';
            btn.disabled = false;
        }

        function copyMessage() {
            const text = document.getElementById('messageOutput').textContent;
            navigator.clipboard.writeText(text).then(() => {
                const btn = event.target;
                btn.textContent = '✅ Copied!';
                setTimeout(() => { btn.textContent = '📋 Copy to Clipboard'; }, 2000);
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/generate-message', methods=['POST'])
def create_message():
    data = request.get_json()
    prompt = data.get('prompt', '')
    name = data.get('name', 'there')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        message = generate_message(prompt, name)
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": f"Generation failed: {str(e)}"}), 500

if __name__ == '__main__':
    print("🚀 WhatsApp CRM running at http://localhost:5052")
    app.run(host='0.0.0.0', port=5052, debug=True)
