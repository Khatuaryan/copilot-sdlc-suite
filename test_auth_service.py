import pytest
from app.services.auth_service import register_user, login_user, logout_user, _users_db, _sessions


@pytest.fixture(autouse=True)
def clear_db():
    _users_db.clear()
    _sessions.clear()
    yield
    _users_db.clear()
    _sessions.clear()


def test_register_user_success():
    user = register_user("john", "john@example.com", "password123")
    assert user.username == "john"
    assert user.email == "john@example.com"
    assert user.password_hash != "password123"


def test_register_duplicate_email():
    register_user("john", "john@example.com", "password123")
    with pytest.raises(ValueError, match="Email already registered"):
        register_user("john2", "john@example.com", "password456")


def test_register_duplicate_username():
    register_user("john", "john@example.com", "password123")
    with pytest.raises(ValueError, match="Username already taken"):
        register_user("john", "john2@example.com", "password456")


def test_login_success():
    register_user("john", "john@example.com", "password123")
    token = login_user("john@example.com", "password123")
    assert token is not None
    assert len(token) == 64


def test_login_wrong_password():
    register_user("john", "john@example.com", "password123")
    with pytest.raises(ValueError, match="Invalid password"):
        login_user("john@example.com", "wrongpassword")


def test_login_user_not_found():
    with pytest.raises(ValueError, match="User not found"):
        login_user("nobody@example.com", "password123")


def test_logout_removes_session():
    register_user("john", "john@example.com", "password123")
    token = login_user("john@example.com", "password123")
    logout_user(token)
    assert token not in _sessions
