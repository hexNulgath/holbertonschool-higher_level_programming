#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request
import json 

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(users)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = {
        data['username']: {
            "name": data['name'],
            "age": data['age'],
            "city": data['city']
        }
    }
    users.update(new_user)
    return jsonify({"message": "User added successfully", "user": new_user}), 201

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<user>")
def get_users(user):
    user_data = users.get(user)
    if user_data:
        return jsonify({user: user_data})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()