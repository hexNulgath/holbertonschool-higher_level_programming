#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request
import json 

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    data = []
    for user in users:
        data.append(user)
    return jsonify(data)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    new_user = {
            "username": data['username'],
            "name": data['name'],
            "age": data['age'],
            "city": data['city']
    }
    users[new_user['username']] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<user>", methods=['GET'])
def get_users(user):
    user_data = users.get(user)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()