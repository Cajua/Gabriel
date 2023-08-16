from flask import Flask, request, jsonify
from dotenv import load_dotenv
from auth import authenticate_request
from connection_gpt import OpenAI_API

load_dotenv()  # Carrega variáveis do arquivo .env

app = Flask(__name__)

@app.route('/conversation', methods=['POST'])
def conversation_endpoint():
    auth_response = authenticate_request()
    if auth_response:
        return auth_response
    
    data = request.json
    messages = data.get('messages')
    
    if not messages:
        return jsonify({"error": "Messages are required"}), 400
    
    try:
        api = OpenAI_API()
        response = api.conversation(messages)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
