from .models import Discount
from .exceptions import DiscountNotFoundError
from datetime import datetime

class DiscountManager:
    def __init__(self):
        self.discounts = {}

    def add_discount(self, discount):
        self.discounts[discount.product_id] = discount

    def remove_discount(self, product_id):
        if product_id not in self.discounts:
            raise DiscountNotFoundError(f"Discount for product {product_id} not found")
        del self.discounts[product_id]

    def get_active_discounts(self):
        now = datetime.now()
        return [
            d for d in self.discounts.values() 
            if d.is_active and d.start_date <= now <= d.end_date
        ]

    def get_discount(self, product_id):
        discount = self.discounts.get(product_id)
        if not discount:
            raise DiscountNotFoundError(f"Discount for product {product_id} not found")
        return discount