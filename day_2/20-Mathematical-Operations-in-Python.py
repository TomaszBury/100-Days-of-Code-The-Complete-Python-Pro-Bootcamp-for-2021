#20. Mathematical Operations in Python

print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(type(6 / 3))

print(2 ** 2)
print(2 ** 8)

i = 16

while i > 0:
    print(f"Exponent {i} base is 2 = {2 ** i} ")
    i -= 1

'''
PEMDAS
'''
#Parentheses, ()
#Exponents, **
#Multiplication * 
#Division, /
#Addition + 
#Subtraction. -

print(3*3 + 3 / 3 - 3)
print(str(type(3*3)) + " " + str(type(3 / 3)) + " " + str(type( - 3)))
print(str(3*3) + " " + str(3/3) + " -3")

print(3 * (3 + 3 / 3 - 3))
print(3 * (3 + 3) / 3 - 3)
