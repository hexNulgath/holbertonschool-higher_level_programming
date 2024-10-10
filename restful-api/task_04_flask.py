#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user_data = users.get(username)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    new_user = {
        "username": data['username'],
        "name": data.get('name', ''),
        "age": data.get('age', None),
        "city": data.get('city', '')
    }

    users[new_user['username']] = new_user

    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run(debug=True)
