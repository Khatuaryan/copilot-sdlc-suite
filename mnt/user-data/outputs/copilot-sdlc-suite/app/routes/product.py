from flask import Blueprint, request, jsonify
from app.services.order_service import _products_db, get_product
from app.models.product import Product

product_bp = Blueprint("product", __name__)


@product_bp.route("/", methods=["GET"])
def list_products():
    category = request.args.get("category")
    products = list(_products_db.values())
    if category:
        products = [p for p in products if p.category == category]
    return jsonify([p.to_dict() for p in products]), 200


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product_detail(product_id):
    try:
        product = get_product(product_id)
        return jsonify(product.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@product_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    product_id = len(_products_db) + 1
    product = Product(
        id=product_id,
        name=data["name"],
        description=data["description"],
        price=data["price"],
        stock=data["stock"],
        category=data["category"],
    )
    _products_db[product_id] = product
    return jsonify(product.to_dict()), 201
