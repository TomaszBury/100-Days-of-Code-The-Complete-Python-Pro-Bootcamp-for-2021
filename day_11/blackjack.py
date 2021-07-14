############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
############### Blackjack Project #####################
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.
############### Our Blackjack House Rules #####################
#Hint 1: Go to this website and try out the Blackjack game:
# https://games.washingtonpost.com/games/blackjack/
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
answer = ""
computer_cards = []
human_cards = []

def deal_cards(deck_user,cards_s):
    deck_user.append(random.choice(cards_s))

def sum_cards(user_deck):
    sum = 0
    for card in user_deck:
        sum += card
    return sum

def check_for_loser(deck_of_cards):
    if sum_cards(deck_of_cards) > 21:
        return False
    else:
        return True

deal_cards(human_cards,cards)
deal_cards(human_cards,cards)
deal_cards(computer_cards,cards)

print(f"Player cards: {sum_cards(human_cards)} <:-:> Dealer cards: {sum_cards(computer_cards)}")

if check_for_loser(human_cards) and check_for_loser(computer_cards):
    answer = input("Hit or Stand? (H/S)").strip().lower()
    if answer == "h":
        deal_cards(human_cards)
    elif answer == "s":
        print("You did great!")

