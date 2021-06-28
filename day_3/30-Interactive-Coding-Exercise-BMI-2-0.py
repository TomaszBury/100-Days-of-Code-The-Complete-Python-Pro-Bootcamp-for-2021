#30. [Interactive Coding Exercise] BMI 2.0

'''
Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.

https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese. 
'''
weigh = int(input("What is your weight in kg?:\n"))
height = float(input("What is your height?:\n"))

BMI = int( weigh / height ** 2)
#print(BMI)

if BMI < 18.5:
    print("Under 18.5 they are underweight")
    print(f"To be normal weight you are missing: {19*height**2 - weigh:.2f}")
elif BMI < 25:
    print("Over 18.5 but below 25 they have a normal weight")
elif BMI < 30:
    print("Over 25 but below 30 they are slightly overweight")
    print(f"To be normal weight you need to loose: {weigh- 24.9*(height**2):.2f}")
    print(f"To be clinically obese you are missing: {weigh - 35.1*height**2:.2f}")
elif BMI < 35:
    print("Over 30 but below 35 they are obese")
    print(f"To be normal weight you need to loose: {weigh- 24.9*(height**2):.2f}")
    print(f"To be clinically obese you are missing: {weigh - 35.1*height**2:.2f}")
else:
    print("Above 35 they are clinically obese.")
    print(f"To be normal weight you need to loose: {weigh- 24.9*(height**2):.2f}")