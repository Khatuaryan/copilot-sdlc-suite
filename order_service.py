from app.models.order import Order
from app.models.product import Product

_orders_db = {}
_products_db = {}


def get_product(product_id: int) -> Product:
    product = _products_db.get(product_id)
    if not product:
        raise ValueError(f"Product {product_id} not found")
    return product


def place_order(user_id: int, cart: list) -> Order:
    """
    cart: list of {"product_id": int, "quantity": int}
    """
    items = []
    for entry in cart:
        product = get_product(entry["product_id"])
        product.reduce_stock(entry["quantity"])
        items.append({
            "product_id": product.id,
            "quantity": entry["quantity"],
            "price": product.price,
        })

    order_id = len(_orders_db) + 1
    order = Order(id=order_id, user_id=user_id, items=items)
    _orders_db[order_id] = order
    return order


def get_order(order_id: int) -> Order:
    order = _orders_db.get(order_id)
    if not order:
        raise ValueError(f"Order {order_id} not found")
    return order


def cancel_order(order_id: int) -> Order:
    order = get_order(order_id)
    order.cancel()
    return order
