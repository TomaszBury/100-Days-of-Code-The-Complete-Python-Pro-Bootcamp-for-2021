import art
import os
def clear():
    os.system('CLS')
#Calculator

#Add
def add(n1, n2):
    return n1 + n2
#Substract
def substract(n1,n2):
    return n1 - n2
#Multiply
def multiply(n1,n2):
    return n1 * n2
#Divide
def divide(n1,n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

clear()
print(art.logo)

num1 = float(input("What's the first number?:\n"))
num2 = float(input("What's is the second number:\n"))
num3 = 0
next_calculations = True

oper = ""
for key in operation:
    oper += key + " "
print(oper)

operation_sympol = input("Pick an operation from the line above:\n")

function = operation[operation_sympol]
answer_one = function(num1,num2)

print(f"{num1} {operation_sympol} {num2} = {answer_one:0.2f}")

while next_calculations:
    clear()
    continue_calculations = input(f"Type 'y' to continue calculating with {answer_one:0.2f}, or type 'n' to exit.:\n").strip().lower()
    if continue_calculations == "y":
        operation_sympol = input("Pick an operation:\n")
        num3 = float(input("What's the next number?:\n"))
        function = operation[operation_sympol]
        answer_two = function(answer_one,num3)
        print(f"{answer_one} {operation_sympol} {num3} = {answer_two:0.2f}")
        answer_one = answer_two
    else:
        next_calculations = False