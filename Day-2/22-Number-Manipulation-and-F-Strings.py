#22. Number Manipulation and F Strings in Python

print(8/3)
print(round(8/3))
print(round(8/3,2))
print()

print(8 // 3)
print("8 // 3")
print(type(8 // 3))
print(type(4/2))
print()

result = 4 / 2
result /= 2

print(result)
print(type(result))
print()

score = 0
score +=1
print(score)
print(type(score))
print("you'r scoris is: " + str(score))
print()
print()

#f-string
height = 1.8
isWinning = True

print(f"you'r score is: {score}, your height is {height}, you ate winning is {isWinning}")