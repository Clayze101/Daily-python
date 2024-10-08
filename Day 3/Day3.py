print("Welcome to the rollercoaster ride!! ")
height = int(input("WHat is your height in cm? "))
bill = 0

if height >= 120:
    print("Your can get a ticket ")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 50

    elif age <= 18:
        bill = 70

    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")

    else:
        bill = 120

    wants_photo = input("Do you want to have a photo take? Type y if yes and n if no ")
    if wants_photo == "y":
        bill += 30
    else:
        print("You dont have to pay more")

    print(f"Your total bill is: {bill}Rs")
else:
    print("You cannot get a ticket ")
