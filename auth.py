from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, login_user, logout_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    try:
        user = register_user(
            username=data["username"],
            email=data["email"],
            password=data["password"],
        )
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    try:
        token = login_user(email=data["email"], password=data["password"])
        return jsonify({"token": token}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401


@auth_bp.route("/logout", methods=["POST"])
def logout():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    logout_user(token)
    return jsonify({"message": "Logged out successfully"}), 200
