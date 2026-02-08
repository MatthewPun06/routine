from user_queries import *;
from flask import Blueprint, request, jsonify

# Define a Blueprint for user-related routes
user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users", methods=["GET"])
def list_users():
    users = get_all_users()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

# GET one user
@user_routes.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name})

# POST create user
@user_routes.route("/users", methods=["POST"])
def create_user_route():
    data = request.json
    user = create_user(data["email"], data["name"], data["password"], data["age"])
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201