#28. [Interactive Coding Exercise] Odd or Even? Introducing the Modulo

'''
https://replit.com/@appbrewery/day-3-1-exercise
'''

'''
Instructions

Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder. 
'''
import random

random_number = 0
for i in range(0,39):
    random_number = random.randint(1,199)
    if random_number % 2 == 0:
        print(f"This is an even number:\t{random_number:3}.")
    else:
        print(f"This is an odd number:\t{random_number:3}.")

print("<><><><><><><><><<><><><><><><><><><><><>")

number_to_test = int(input("What number you want to test if it is Even of Odd?:\n"))

if number_to_test % 2 == 0:
    print("This is an even number.\n")
else:
    print("This is an odd number.\n")