try:
    number = int(input("Enter a number"))
    print("The number is entred is",number)
except ValueError as x:
    print("Expetion",x)