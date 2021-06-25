#18. Type Error, Type Checking and Type Conversion
print("What is you'r name?:\n")
#num_char = len(input("What is yo'r name?\n"))
num_char = "Gemini"
#print("You'r name has " + num_char + " characters.")
'''
print("You'r name has " + num_char + " characters.")
TypeError: can only concatenate str (not "int") to str
'''
print(type(num_char))

new_num_char = str(num_char)

print(type(new_num_char))

print("You'r name has " + new_num_char + " characters.")

a = 123
print(type(a))
a = str(123)
print(type(a))

a = float(132)
print(type(a))

print(70 + float("100.5"))
print(type(70 + float("100.5")))

print(str(70) + str(100))
print(type(str(70) + str(100)))