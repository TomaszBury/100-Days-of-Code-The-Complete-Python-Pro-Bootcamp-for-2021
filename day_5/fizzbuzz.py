#53. [Interactive Coding Exercise] The FizzBuzz Job Interview Question
'''
You are going to write a program that automatically prints the solution to the FizzBuzz game.
    Your program should print each number from 1 to 100 in turn.
    When the number is divisible by 3 then instead of printing the number it should print "Fizz".
    `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
      `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
e.g. it might start off like this:
'''
#Write your code below this row 👇
print_statement = ""

for number in range(1,101,1):
    if number % 3 == 0:
        print_statement = "Fizz"

    if number % 5 == 0:
        print_statement += "Buzz"

    if print_statement == "":
        print(number)
    else:
        print(print_statement)
        print_statement = ""

print("-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-")
print("The lame way to do this:")
print("-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-")

for number in range(1,101):
    if number % 3 and number % 5 == 0:
        print("Fizz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

print("-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-")
print("double check - go over (something) for a second time to ensure that it is accurate or safe.")
print("-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-")
awesome_list = []
lame_list = []

for number in range(1,101,1):
    if number % 3 == 0:
        print_statement = "Fizz"

    if number % 5 == 0:
        print_statement += "Buzz"

    if print_statement == "":
        awesome_list.append(number)
    else:
        awesome_list.append(print_statement)
        print_statement = ""

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        lame_list.append("FizzBuzz")
    elif number % 3 == 0:
        lame_list.append("Fizz")
    elif number % 5 == 0:
        lame_list.append("Buzz")
    else:
        lame_list.append(number)

for i in range(0,100,1):
    if awesome_list[i] != lame_list[i]:
        print(F"{awesome_list[i]}:\t{lame_list[i]} \t {i}If you won't be a good example, then you'll have to be a horrible warning.\nYou snollygoster!")