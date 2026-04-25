from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# 🔐 MUST MATCH TEST EXPECTATIONS
users = {
    "admin": generate_password_hash("admin123")
}

# ✔ VERIFY FUNCTION (CRITICAL)
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return username
    return None


# 🔒 PROTECTED ROUTE
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "OK", 200


if __name__ == "__main__":
    app.run()
