from flask import Flask, jsonify, request

app = Flask(__name__)

# in-memory data (empty saxla, checker üçün)
users = {}

# 1. ROOT
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# 2. DATA (usernames list)
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# 3. STATUS
@app.route("/status")
def status():
    return "OK"

# 4. GET USER BY USERNAME
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# 5. ADD USER (POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # invalid JSON
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # username yoxdursa
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # add user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
