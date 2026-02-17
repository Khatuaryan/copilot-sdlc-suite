from datetime import datetime


class Order:
    def __init__(self, id, user_id, items, created_at=None):
        self.id = id
        self.user_id = user_id
        self.items = items  # list of {"product_id": x, "quantity": y, "price": z}
        self.status = "pending"
        self.created_at = created_at or datetime.utcnow()
        self.total = sum(item["price"] * item["quantity"] for item in items)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "items": self.items,
            "status": self.status,
            "total": self.total,
            "created_at": self.created_at.isoformat(),
        }

    def mark_paid(self):
        if self.status != "pending":
            raise ValueError(f"Cannot mark order as paid. Current status: {self.status}")
        self.status = "paid"

    def cancel(self):
        if self.status == "shipped":
            raise ValueError("Cannot cancel a shipped order")
        self.status = "cancelled"

    def __repr__(self):
        return f"<Order {self.id} - {self.status}>"
