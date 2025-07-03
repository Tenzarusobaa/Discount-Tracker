from dataclasses import dataclass
from datetime import datetime

# IntelliSense assisted comments
# This file contains the data models for the e-commerce application.
# It includes models for products, orders, customers, and discounts.
# Each model is represented as a dataclass for easy instantiation and management.


@dataclass
class Discount: # Represents a discount applied to a product
    product_id: str
    discount_percent: float
    start_date: datetime
    end_date: datetime 
    is_active: bool = True
    