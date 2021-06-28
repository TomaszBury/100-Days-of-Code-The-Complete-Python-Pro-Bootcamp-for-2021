#45. Day 4 Project: Rock Paper Scissors
#https://replit.com/@appbrewery/rock-paper-scissors-start

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = ["rock","paper","scissors"]
human = input("Chose rock / paper / scissors:\n").lower().strip()
mac = choices[random.randint(0,2)]

if human != "rock" and human != "paper" and human != "scissors":
    print("You typed an invalid input, dummy!\nrock / paper / scissors\nIt is not that hard!")
else:
    if mac == "rock":
        print(f'''Mac chosen rock: 
        {rock}
        ''')
    elif mac == "paper":
        print(f'''Mac chosen paper: 
        {paper}
        ''')
    elif mac == "scissors":
        print(f'''Mac chosen scissors: 
        {scissors}
        ''')

if mac == human:
    print("Draw")
elif human == "rock" and mac == "scissors":
    print("Human won!")
elif human == "scissors" and mac == "paper":
    print("Human won!")
elif human == "paper" and mac == "rock":
    print("Human won!")
else:
    print("Mac won!")

#print(f"{human}:{mac}")