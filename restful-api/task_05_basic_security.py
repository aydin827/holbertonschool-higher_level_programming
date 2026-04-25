from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# JWT config
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Basic Auth
auth = HTTPBasicAuth()

# users (username: data)
users = {
    "admin": {
        "password": generate_password_hash("admin123"),
        "role": "admin"
    },
    "john": {
        "password": generate_password_hash("1234"),
        "role": "user"
    }
}

# 🔐 BASIC AUTH VERIFY
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username

# 🔑 LOGIN → JWT TOKEN
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"username": username, "role": user["role"]})

    return jsonify({"access_token": access_token})

# 🔒 BASIC AUTH PROTECTED
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth Success!"

# 🔒 JWT PROTECTED
@app.route("/profile")
@jwt_required()
def profile():
    user = get_jwt_identity()
    return jsonify(user)

# 👑 ADMIN ONLY
@app.route("/admin")
@jwt_required()
def admin():
    user = get_jwt_identity()

    if user["role"] != "admin":
        return jsonify({"error": "Access denied"}), 403

    return jsonify({"message": "Welcome Admin!"})


if __name__ == "__main__":
    app.run()
