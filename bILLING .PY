
from collections import deque
billing_queue = deque()
def add_customer():
    name = input("Enter customer name: ")
    n = int(input("Enter number of items: "))

    items = []
    total = 0

    for i in range(n):
        item = input(f"Enter item {i+1} name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        amount = price * quantity
        total += amount

        items.append((item, price, quantity, amount))

    customer = {
        "name": name,
        "items": items,
        "total": total
    }

    billing_queue.append(customer)
    print("\nCustomer added to billing queue successfully!")
def display_queue():
    if not billing_queue:
        print("\nNo customers in the queue.")
    else:
        print("\nCustomers Waiting for Billing:")
        for i, customer in enumerate(billing_queue, 1):
            print(f"{i}. {customer['name']}")
def process_billing():
    if not billing_queue:
        print("\nNo customers available for billing.")
        return

    customer = billing_queue.popleft()

    print("\n========== GROCERY BILL ==========")
    print("Customer Name:", customer["name"])
    print("Item       Price  Qty  Amount")

    for item, price, qty, amount in customer["items"]:
        print(f"{item:<10} {price:<6.2f} {qty:<4} {amount:.2f}")
    print("Total Amount: Rs.", customer["total"])
    print("Billing Completed!")


# Main program
while True:
    print("\n===== GROCERY BILLING SYSTEM =====")
    print("1. Add Customer")
    print("2. Display Queue")
    print("3. Process Billing")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_customer()

    elif choice == '2':
        display_queue()

    elif choice == '3':
        process_billing()

    elif choice == '4':
        print("Thank you for using Grocery Billing System!")
        break
    else:
        print("Invalid choice! Please try again.")