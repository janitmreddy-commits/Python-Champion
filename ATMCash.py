print("ATM Cash Dispenser")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customer_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Enter your name")
    amount = int(input("Enter withdrawal"))
    if amount <= 0:
     print("Invalid input")
     continue
    print(f"Dispensing {amount} units for {name}:")
    remaining = amount
    idx = 0
    while idx <= 6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1

        count = remaining // value
        if count >0:
          print(f" {count} x {value}unit note(s)= {count * value}")
          remaining -= count * value
          if value == 100: total_100 += count
          elif value == 50: total_50 += count
          elif value == 20: total_20 += count
          elif value == 10: total_10 += count
          elif value == 5: total_5 += count
          else: total_1 += count

        idx += 1

    customer_served += 1
    total_dispensed = 1
    print("Completed")     
    again = input("Next,yes or no").strip().lower()
    if again == "no": serving = False

print(f"\nCustomers served : {customer_served}")

print(f"Total dispensed : {total_dispensed} units")

print("ATM session closed. Goodbye!")
          