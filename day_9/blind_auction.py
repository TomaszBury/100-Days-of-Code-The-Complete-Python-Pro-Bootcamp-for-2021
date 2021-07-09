import art
#from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(f"{art.logo}\n")
bids = {}
bidding = True
def add_bid(name,bid):
    bids[name] = bid

def ask_for_bid():
    name = input("What is your name:\n")
    bid = input("What is your bid:\n")
    add_bid(name,bid)

def next_bidder():
    bidder = input("\nAre there any more bidders (Yes/No)?\n").strip().lower()
    if bidder == "no":
        return False
def find_winnrer():
    winner = ""
    for key in bids:
        if len(bids) >

while bidding:
    ask_for_bid()
    bidding = next_bidder()
    if bidding == False:
        find_winnrer()