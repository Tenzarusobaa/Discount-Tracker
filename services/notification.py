#IntelliSense assisted comments

from datetime import datetime, timedelta

def check_expiring_discounts(discounts, days_threshold=3): 
    # This function checks for discounts that are expiring within a specified number of days.
    # It returns a list of discounts that are active and have an end date within the threshold.
    now = datetime.now()
    threshold_date = now + timedelta(days=days_threshold)
    return [
        d for d in discounts
        if d.end_date <= threshold_date and d.is_active
    ]