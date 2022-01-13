from game_data import data
from art import logo
from art import vs
from random import randint

# print("\nWho has more instagram followers in millions:")
compareA = 0
compareB = 0
while compareA == compareB:
    compareA = randint(0,len(data))
    compareB = randint(0,len(data))
game_on = True
user_score = 0

print(logo)

while game_on:
    print(f"A: {data[compareA]['name']},\n profesion: {data[compareA]['description']},\n country of birth: {data[compareA]['country']}")

    print(vs)

    print(f"B: {data[compareB]['name']},\n profesion: {data[compareB]['description']},\n country of birth: {data[compareB]['country']}")

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
    correct_answer = ""
    if data[compareA]['follower_count'] > data[compareB]['follower_count']:
        correct_answer = "a"
        compareB = randint(0,len(data))
    else:
        correct_answer = "b"
        compareA = compareB
        compareB = randint(0,len(data))

    if user_answer == correct_answer:
        print("You win")
        user_score += 1
        print(f"Curren score: {user_score}")
        game_on = True

    else:
        print(F"Sorry, that's wrong. Final score: {user_score}")
        game_on = False

# print(data[])