print ("======================")
print ("chooe the vehicle")
print ("1. car")
print("2. bike")
choose = int(input("Enter 1 or 2"))
print()

if choose == 1:
    print("choose the car type")
    print("1-sedan")
    print("2-suv")

    car = int(input("Enter 1 or 2"))
    if car == 1:
        print("You choose a sedan car")
    else:
        print("You choose a suv car")
elif choose == 2:
    print("choose the bike type")
    print("1-scooty")
    print("2-mountain bike")

    bike = int(input("Enter 1 or 2"))
    if bike == 1:
       print("You choose a scooty bike") 
    else:
        print("You choose a mountain bike")   
