#23. [Interactive Coding Exercise] Life in Weeks

'''
https://replit.com/@appbrewery/day-2-3-exercise

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

    You have x days, y weeks, and z months left. 

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops. 
'''

'''
https://cdn.fs.teachablecdn.com/RjqBViZQpyVTv7XY6cfA
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_to_live = 90 - int(age)

days = years_to_live * 365
weeks = years_to_live * 52
months = years_to_live * 12

message = f"You have {days}, {weeks} and {months} left."

print(message)  