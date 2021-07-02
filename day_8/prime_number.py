'''
Prime Numbers
Instructions

Prime numbers are numbers that can only be cleanly divided by itself and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H

Here are the numbers up to 100, prime numbers are highlighted in yellow:

https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw
'''

#Write your code below this line 👇
'''
def prime_checker(number):
    number_divisions = 0
    #print(number)
    if number % number == 0 and number > 1:
        for i in range(2,number+1):
            if number % i == 0:
                number_divisions += 1
            #print(f"i:{i}, number of divisions:{number_divisions}")
        if number_divisions == 1:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
    else:
        print("It's not a prime number.")
'''
def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
