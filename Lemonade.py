def greet_customer():
    print("Welcome to fresh Lemonade Stand!")
    print("Fresh Lemonade for you")

greet_customer()
price_per_cup = float(input("Enter cup in dollars"))
cups_sold = int(input("Enter the number of cups sold"))

def calculate_total(price,cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost,2)
print("Total_cost:", rounded_total)
amount_paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(paid,total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
round_change = round(change_due,2)

print("====== LEMONADE STAND RECEIPT ======")
print("Price Per Cup:", price_per_cup)
print("Cups Sold:", cups_sold)
print("total_cost:", rounded_total)
print("Amount Paid:",amount_paid)
print("Change Due:",change_due)