from core.discount_manager import DiscountManager
from core.models import Discount
from datetime import datetime

#IntelliSense assisted comments
# This script provides a command-line interface for managing discounts in an e-commerce application.

def main():
    manager = DiscountManager()
    
    while True:
        print("\nDiscount Tracker System")
        print("1. Add Discount")
        print("2. Remove Discount")
        print("3. List Active Discounts")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            try:
                product_id = input("Product ID: ")
                discount_percent = float(input("Discount (%): "))
                start_date = datetime.strptime(input("Start Date (YYYY-MM-DD): "), "%Y-%m-%d")
                end_date = datetime.strptime(input("End Date (YYYY-MM-DD): "), "%Y-%m-%d")
                
                # Basic validation
                if discount_percent <= 0 or discount_percent > 100:
                    print("Error: Discount must be between 0-100%")
                    continue
                if start_date >= end_date:
                    print("Error: Start date must be before end date")
                    continue
                
                discount = Discount(product_id, discount_percent, start_date, end_date)
                manager.add_discount(discount)
                print(f"Added discount for {product_id}")
            except ValueError as e:
                print(f"Invalid input: {e}")
        
        elif choice == "2":
            product_id = input("Product ID to remove: ")
            try:
                manager.remove_discount(product_id)
                print(f"Removed discount for {product_id}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            active = manager.get_active_discounts()
            if active:
                for discount in active:
                    print(f"{discount.product_id}: {discount.discount_percent}% until {discount.end_date.date()}")
            else:
                print("No active discounts")
        
        elif choice == "4":
            break

if __name__ == "__main__":
    main()