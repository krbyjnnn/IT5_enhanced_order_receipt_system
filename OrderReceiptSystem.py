import time
from datetime import date, datetime

time.sleep(2)
now = datetime.now()

while True:
    print("=" * 12,"ORDER RECEIPT SYSTEM", "=" * 12, "\n")
    print("1. Enter an order")
    print("2. View products")
    print("3. Exit", "\n")
    print("=" * 46)

    choice = int(input("What do you want to do? "))

    if choice == 1:
        customer_name = input("Enter customer name: ")

        food_items = input("Enter food items: ")
        items_split = food_items.split(",")

        price = float(input("Enter Price: "))
        while price <= 0:
            print("Price must be greater than 0.")
            price = float(input("Enter Price: "))

        quantity = int(input("Enter Quantity: "))  
        while quantity <= 0:
            print("Quantity must be greater than 0.")
            quantity = int(input("Enter quantity: "))

        total_amount = price * quantity

        print("-" * 46)
        cash_amount = float(input("Enter cash amount: "))
        while cash_amount < total_amount:
            print("Amount must be greater than the total amount.")
            cash_amount = float(input("Enter cash amount: "))
        print("-" * 46)

        print("\nProcessing your order...\n")

        print("=" * 15, "ORDER RECEIPT", "=" * 16, "\n")

        print("Customer Name :", customer_name.strip().title())
        print("Uppercase     :", customer_name.upper())
        print("Name Length   :", len(customer_name),"\n")

        print("Ordered Items :", " | ".join(items_split), "\n")

        print(f"Price         : PHP {price:.2f}" )
        print("Quantity      :", quantity, "\n")

        print("-" * 46)
        print(f"Total Amount  : PHP {total_amount:.2f}")
        print("-" * 46)
        print(f"Cash          : PHP {cash_amount:.2f}")
        change = cash_amount - total_amount
        print(f"Change        : PHP {change:.2f}")
        print("-" * 46)

        print("Date          :", date.today().strftime("%B %d, %Y"))
        print("Time          :", now.strftime("%I:%M %p"))

        print("=" * 46)
        print("           THANK YOU FOR ORDERING!")
        print("=" * 46)

    elif choice == 2:
        print("=" * 46)
        print("                PRODUCTS LISTS")
        print("=" * 46, "\n")
        print("1. Rice  - PHP 55.00")
        print("2. Juice - PHP 20.00")
        print("3. Egg   - PHP 10.00", "\n")
        print("=" * 46)

    else:
        print("=" * 46)
        print("            THANK YOU AND GOODBYE!")
        print("=" * 46)
        break