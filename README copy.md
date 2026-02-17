# E-Commerce Backend API

A simple Python/Flask e-commerce backend used as a test project for the Copilot SDLC Assist Suite.

## Project Structure

```
app/
├── models/
│   ├── user.py       # User model
│   ├── product.py    # Product model
│   └── order.py      # Order model
├── routes/
│   ├── auth.py       # Register, login, logout endpoints
│   ├── user.py       # User profile endpoints
│   └── product.py    # Product listing and creation endpoints
├── services/
│   ├── auth_service.py    # Authentication logic
│   └── order_service.py   # Order placement and management
tests/
└── test_auth_service.py   # Auth service unit tests
```

## Endpoints

| Method | Endpoint            | Description          |
|--------|---------------------|----------------------|
| POST   | /auth/register      | Register a new user  |
| POST   | /auth/login         | Login and get token  |
| POST   | /auth/logout        | Logout               |
| GET    | /users/me           | Get current user     |
| PUT    | /users/me           | Update current user  |
| GET    | /products/          | List all products    |
| GET    | /products/<id>      | Get product detail   |
| POST   | /products/          | Create a product     |

## Known Gaps (intentional for agent testing)

- `order_service.py` has no tests
- `order.py` model has no tests
- `product.py` model has no tests
- No input validation on user update endpoint
- No authentication check on product creation endpoint
- Order placement has no payment integration
