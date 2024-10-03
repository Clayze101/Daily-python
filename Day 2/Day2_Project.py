print("WellCome to Tip Calculater")

Bill = float(input("What was the tota bill? "))
Tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
ppl = int(input("How many people to split the bill? "))


Final_Bill = float(Bill) * ((float(Tip) / 100) + 1)
Final_Bill = round(Final_Bill, 3)
Bill_Per_Person = Final_Bill / ppl
Bill_Per_Person = round(Bill_Per_Person, 2)
print(f"Each person should pay is {Bill_Per_Person}")

