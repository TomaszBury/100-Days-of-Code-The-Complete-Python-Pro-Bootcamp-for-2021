#21. [Interactive Coding Exercise] BMI Calculator
'''
https://replit.com/@appbrewery/day-2-2-exercise
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should convert the result to a whole number. 

https://en.wikipedia.org/wiki/Body_mass_index
'''

weight = int(input("What is you weight(kg)?:\n"))
height = float(input("What is your height in meters?:\n"))

BMI = weight / height ** 2

print(f"You'r BMI is {int(BMI)}")

BMI_Prime = BMI / 25

if BMI < 15:
    print("Very severely underweight ")
elif BMI < 16:
    print("Severely underweight ")
elif BMI < 18.5:
    print("Underweight ")
elif BMI < 25:
    print("Normal (healthy weight) ")
elif BMI < 30:
    print("Overweight ")
elif BMI < 35:
    print("Obese Class I (Moderately obese) ")
elif BMI < 40:
    print("Obese Class II (Severely obese) ")
else:
    print("Obese Class III (Very severely obese). YOU ARE DONE!")

ideal_weight = 25 * height ** 2

print("You should weight: " + str(int(ideal_weight)) + " You will loose: " + str(weight-int(ideal_weight)))