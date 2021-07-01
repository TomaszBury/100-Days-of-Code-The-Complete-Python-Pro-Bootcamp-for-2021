'''
# Review: 
# Create a function called greet(). 
def greet_with_name(name,location):

# Write 3 print statements inside the function.
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"How is the weather in {location}?")
# Call the greet() function and run your code.
greet_with_name(input("What is you'r name?:\n"),input("Whera are you now?:\n"))
'''

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location}?")

greet_with(input("Whatis you'r name?:\n"),input("What is you'r location?:\n"))

greet_with(location="Graz",name="Emilia")