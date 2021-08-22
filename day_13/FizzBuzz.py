# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print(f"{number}: FizzBuzz")
#   elif number % 3 == 0:
#     print(f"{number}: Fizz")
#   elif number % 5 == 0:
#     print(f"{number}: Buzz")
#   else:
#     print(number)
# print_text = ""
# for number in range(9,16):
#     if number % 3 == 0:
#         print_text ="Fizz"
#     if number % 5 == 0:
#         print_text +="Buzz"
#     if print_text == "":
#         print_text = str(number)
#     # print(f"Number: {number}, calc: {print_text}")
#     print(print_text)
#     print_text = ""
how_many_Fizz = 0
how_many_Buzz = 0
how_many_FizBuzz = 0
how_many_none = 0
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    # print(f"{number}: FizzBuzz")
    how_many_FizBuzz += 1
  elif number % 3 == 0:
    # print(f"{number}: Fizz")
    how_many_Fizz += 1
  elif number % 5 == 0:
    # print(f"{number}: Buzz")
    how_many_Buzz += 1
  else:
    # print(number)
    how_many_none += 1

print(f"""How many:
FizzBuzz: {how_many_FizBuzz}
Buzz: {how_many_Buzz}
Fizz: {how_many_Fizz}
None: {how_many_none}
""")