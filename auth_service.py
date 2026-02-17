import hashlib
import secrets
from app.models.user import User

# Simulated in-memory user store
_users_db = {}
_sessions = {}


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username: str, email: str, password: str) -> User:
    if email in [u.email for u in _users_db.values()]:
        raise ValueError("Email already registered")
    if username in [u.username for u in _users_db.values()]:
        raise ValueError("Username already taken")

    user_id = len(_users_db) + 1
    user = User(
        id=user_id,
        username=username,
        email=email,
        password_hash=hash_password(password),
    )
    _users_db[user_id] = user
    return user


def login_user(email: str, password: str) -> str:
    user = next((u for u in _users_db.values() if u.email == email), None)
    if not user:
        raise ValueError("User not found")
    if user.password_hash != hash_password(password):
        raise ValueError("Invalid password")

    token = secrets.token_hex(32)
    _sessions[token] = user.id
    return token


def get_user_from_token(token: str) -> User:
    user_id = _sessions.get(token)
    if not user_id:
        raise ValueError("Invalid or expired session")
    return _users_db[user_id]


def logout_user(token: str):
    if token in _sessions:
        del _sessions[token]
