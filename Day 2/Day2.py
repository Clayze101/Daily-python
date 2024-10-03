# Subscripting
# print("Hello"[0])
# print("Hello"[-1])

# String
# print("123"+"345")

# Integer - Whole Number
# print(123 + 345)

# To print larger integers 
# print(123_234_345)      

# Float - Decimal Numbers
# print(3.14159)

# Boolean - True & False
# print(True)
# print(False)

# len(123) - type error example

# 4 data types / Type Checking
# print(type("String"))
# print(type(123))
# print(type(3.14))
# print(type(True))

# # Type Conversion
# print(int("123")+ int("456"))

# Practice Question (Try to run the below line of code wthout any error)
# print("Numbers of Letter in your name: " + len(input("Enter your name: ")))

# name_of_user = input("Enter Your Name: ")
# length_of_name = len(name_of_user)

# print(type("Numbers of Letter in your name: ")) # str
# print(type(length_of_name)) # int

# print("Number of letters in your name: " + str(length_of_name))

# Mathematical Operations
# print(69 + 22)
# print(10 - 2)
# print(69 * 10)
# print(2 ** 3) # gives the answer of index
# print(6 / 3)
# print(5 / 3) # when the anser is in decimal
# print(5 // 3) # removes the decimal

# PEMDAS

# ()
# **
# * OR /
# + OR -

# print(3 * 3 + 3 / 3 - 3)
# print(3 * 3 / 3 + 3 - 3)

# Round 
# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(round(bmi, 2))

score = 0
Trophy = 4
is_winning = True

print(score)
# user scores a point
score += 1
print(score)

# f-strings - in python, we can use f-string to insert a variable pr an expression into a string
print(f"Your score is = {score}, Your height is {Trophy}, You are winning ? {is_winning}")

a = int("5") / int(2.7)
print(type(a))