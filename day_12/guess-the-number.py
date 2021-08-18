#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo 
from random import Random
print(logo)

EASY = 10
HARD = 5
NUMBER = random.randint(0,100)



def check_guess(guess):
    if guess > NUMBER:
        return "Too high."
    else:
        return " Too low."

def game():
    print(f"Welcome to the number Guesing Game!")
    print(f"I'm thinking of number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard:\n").lower().strip()

    attempts = 0

    if difficulty == 'hard':
        attempts = HARD
    else:
        attempts = EASY
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number")
        guess = int(input("\tMake a guess:").strip())
        if guess == NUMBER:
            print("You lucky SOB!")
            attempts = -1
        else:
            print(check_guess(guess))
            attempts -= 1

while input("Do you want to play?\n 'y' / 'n'") =='y':
        game()
print("\t\t\tby...")

