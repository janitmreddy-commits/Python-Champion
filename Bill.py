
tables = {1: "Available", 2: "Available",
          3: "Available", 4: "Available"}

menu = {"Burger": 100, "Pizza": 200, "Coffee": 50}
table = int(input("Enter table number: "))

if table in tables and tables[table] == "Available":
    tables[table] = "Occupied"
    print("Table booked!")
else:
    print("Table unavailable!")
total = 0

print("\nMenu:", menu)

while True:
    item = input("Enter item (or done): ").title()

    if item == "Done":
        break

    if item in menu:
        qty = int(input("Enter quantity: "))
        total += menu[item] * qty
    else:
        print("Item not found!")

gst = total * 0.05

print("\n----- BILL -----")
print("Subtotal:", total)
print("GST:", gst)
print("Total:", total + gst)
tables[table] = "Available"
print("Table available again!")