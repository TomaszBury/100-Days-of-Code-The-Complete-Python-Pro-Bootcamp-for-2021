import art
#from replit import clear
import os

def clear():
    os.system('CLS')

#HINT: You can call clear() to clear the output in the console.
print(f"{art.logo}\n")
bids = {}
bidding = True
winner = ""
def add_bid(name,bid):
    bids[name] = bid

def ask_for_bid():
    name = input("What is your name:\n")
    bid = input("What is your bid:\n")
    add_bid(name,int(bid))

def next_bidder():
    bidder = input("\nAre there any more bidders (Y/N)?\n").strip().lower()
    print()
    if bidder == "n":
        return False
    else:
        return True

def find_winnrer():
    highest_bid = 0
    for key, value in bids.items():
        if value > highest_bid:
            highest_bid = value
            winner = key
    print(f"The wienner is: {winner}, with a bid of {highest_bid}")

while bidding:
    ask_for_bid()
    bidding = next_bidder()
    if bidding == False:
        find_winnrer()
    else:
        clear()