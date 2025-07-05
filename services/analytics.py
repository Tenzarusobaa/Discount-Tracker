#IntelliSense assisted comments

def calculate_average_discount(discounts): # This function calculates the average discount percentage from a list of discounts.
    if not discounts:
        return 0.0
    return sum(d.discount_percent for d in discounts) / len(discounts)

def find_max_discount(discounts): # This function fginds the discount with the maximum percentage from a list of discounts.
    return max(discounts, key=lambda d: d.discount_percent, default=None)