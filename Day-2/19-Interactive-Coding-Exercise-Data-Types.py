#19. [Interactive Coding Exercise] Data Types
'''
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
'''

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#print(int(two_digit_number[0]) + int(two_digit_number[1]))

sum = 0

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

for digit in two_digit_number:
    if is_number(digit):
        sum += int(digit)

print(sum)

	
