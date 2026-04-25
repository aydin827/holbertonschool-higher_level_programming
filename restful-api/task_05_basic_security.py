from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# 🔐 users (IMPORTANT: checker bu adları gözləyir)
users = {
    "admin": generate_password_hash("admin123"),
    "user": generate_password_hash("user123")
}

# ✔ BASIC AUTH CHECK
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None


# 🔒 PROTECTED ROUTE (TEST BUNU ÇAĞIRIR)
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Hello, Basic Auth Success!"


# server start
if __name__ == "__main__":
    app.run()
