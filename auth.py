from flask import request, jsonify
import os

SECRET_KEY = os.getenv("APP_SECRET_KEY")

def authenticate_request():
    auth_token = request.headers.get('Authorization')
    if not auth_token or auth_token != SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    return None
