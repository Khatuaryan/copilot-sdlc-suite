from flask import Blueprint, request, jsonify
from app.services.auth_service import get_user_from_token

user_bp = Blueprint("user", __name__)


@user_bp.route("/me", methods=["GET"])
def get_current_user():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        user = get_user_from_token(token)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401


@user_bp.route("/me", methods=["PUT"])
def update_current_user():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        user = get_user_from_token(token)
        data = request.get_json()
        if "username" in data:
            user.username = data["username"]
        if "email" in data:
            user.email = data["email"]
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
