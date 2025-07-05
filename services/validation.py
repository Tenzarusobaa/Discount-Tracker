from core.exceptions import DiscountValidationError
from datetime import datetime

def validate_discount_data(discount_percent, start_date, end_date):
    if discount_percent <= 0 or discount_percent > 100:
        raise DiscountValidationError("Discount must be between 0-100%")
    
    if start_date >= end_date:
        raise DiscountValidationError("Start date must be before end date")
    
    if end_date < datetime.now():
        raise DiscountValidationError("End date cannot be in the past")