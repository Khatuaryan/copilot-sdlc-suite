from datetime import datetime


class Product:
    def __init__(self, id, name, description, price, stock, category, created_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.created_at = created_at or datetime.utcnow()
        self.is_available = stock > 0

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "category": self.category,
            "is_available": self.is_available,
        }

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Insufficient stock")
        self.stock -= quantity
        self.is_available = self.stock > 0

    def __repr__(self):
        return f"<Product {self.name}>"
