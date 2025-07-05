from core.discount_manager import DiscountManager
from core.models import Discount
from services.validation import validate_discount_data
from services.analytics import calculate_average_discount, find_max_discount
from services.notification import check_expiring_discounts
from utils.helpers import parse_date
from utils.logger import setup_logger
import datetime

logger = setup_logger()

def main():
    manager = DiscountManager()
    
    while True:
        print("\nDiscount Tracker System")
        print("1. Add Discount")
        print("2. Remove Discount")
        print("3. List Active Discounts")
        print("4. Show Analytics")
        print("5. Check Expiring Discounts")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            product_id = input("Product ID: ")
            discount_percent = float(input("Discount (%): "))
            start_date = parse_date(input("Start Date (YYYY-MM-DD): "))
            end_date = parse_date(input("End Date (YYYY-MM-DD): "))
            
            try:
                validate_discount_data(discount_percent, start_date, end_date)
                discount = Discount(product_id, discount_percent, start_date, end_date)
                manager.add_discount(discount)
                logger.info(f"Added discount for {product_id}")
            except Exception as e:
                logger.error(f"Error: {e}")
        
        elif choice == "2":
            product_id = input("Product ID to remove: ")
            try:
                manager.remove_discount(product_id)
                logger.info(f"Removed discount for {product_id}")
            except Exception as e:
                logger.error(f"Error: {e}")
        
        elif choice == "3":
            active = manager.get_active_discounts()
            for discount in active:
                print(f"{discount.product_id}: {discount.discount_percent}% until {discount.end_date.date()}")
        
        elif choice == "4":
            active = manager.get_active_discounts()
            avg = calculate_average_discount(active)
            max_discount = find_max_discount(active)
            print(f"Active Discounts: {len(active)}")
            print(f"Average Discount: {avg:.2f}%")
            if max_discount:
                print(f"Highest Discount: {max_discount.product_id} - {max_discount.discount_percent}%")
        
        elif choice == "5":
            expiring = check_expiring_discounts(manager.get_active_discounts())
            if expiring:
                print("Expiring soon:")
                for discount in expiring:
                    days_left = (discount.end_date - datetime.now()).days
                    print(f"{discount.product_id} expires in {days_left} days")
            else:
                print("No expiring discounts")
        
        elif choice == "6":
            break

if __name__ == "__main__":
    main()