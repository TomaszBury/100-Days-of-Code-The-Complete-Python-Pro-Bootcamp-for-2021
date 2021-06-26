#32. Multiple If Statements in Succession

height = int(input("What is you'r height:\n"))
bill = 0

if height >= 120:
    print("You'r going for this ride!")
    age = int(input("What is your age?:\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("Adult ticket are $12.")
    wants_photo = input("Do you want a photo thaken? Y or N:").lower()
    if wants_photo == "y":
        #add $3 to thier bill
        bill += 3
    
    print(f"You'r final ${bill}")
else:
    print("Grow up!!!!!!\n")

