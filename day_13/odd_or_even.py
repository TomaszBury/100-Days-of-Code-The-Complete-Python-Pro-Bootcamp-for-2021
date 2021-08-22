from random import randint, randrange

# number = int(input("Which number do you want to check?"))
even_numbers = []
odd_numbers = []

# for _ in range(1,randint(1,100)):
#     number = randint(1,999)
#     if number % 2 == 0:
#         print(f"This is an even number. {number}, ",end="")
#     else:
#         print(f"\nThis is an odd number. {number}, ", end="")

for _ in range(1,randint(1,100)):
    number = randint(1,999)
    if number % 2 == 0:
        # even_numbers.append(f"This is an even number. {number}, ")
        even_numbers.append(number)
    else:
        # odd_numbers.append(f"This is an odd number. {number}, ")
        odd_numbers.append(number)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")