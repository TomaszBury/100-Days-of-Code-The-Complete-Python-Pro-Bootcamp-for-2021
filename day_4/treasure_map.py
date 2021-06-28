#44. [Interactive Coding Exercise] Treasure Map
#https://replit.com/@appbrewery/day-4-3-exercise
'''
You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list.
When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
'''
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#map[int(position[1])-1][int(position[0])-1] = "X"

if  position[0].isnumeric() and position[1].isnumeric():
    horizontal = int(position[0]) - 1
    vertical = int(position[1]) - 1
    if horizontal <=2 and vertical <= 2:
        map[vertical][horizontal] = "X"
    else:
        print("Out of map!")
else:
    print("Out of map!")


#print(f"horizontal:{horizontal}, vertical:{vertical}")






#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")