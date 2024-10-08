print("Welcome to Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you wamt extra cheese? Y or N: ")

bill = 0
if size == "S" or "M" or "L":
    if size == "S":
        bill = 150
            
    elif size == "M":
        bill = 250

    elif size == "L":
        bill = 350

    if pepperoni == "Y":
        if size == "S":
            bill += 20
        else:
            bill += 30

    if extra_cheese == "Y":
        bill += 20

else:
    print("You typed the wrong inputs ")



print(f"Your total bill is {bill}Rs")