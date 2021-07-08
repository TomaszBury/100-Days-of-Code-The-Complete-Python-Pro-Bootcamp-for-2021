programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
    }
for key in programming_dictionary:
    print(programming_dictionary[key])

print(f"\n{programming_dictionary['Bug']}\n")

#adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"

for key in programming_dictionary:
    print(key)

empty_dictionary = {}
programming_dictionary = {}
print(programming_dictionary)

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again"
    }
print(programming_dictionary)
programming_dictionary["Bug"] = "A moth in you'r computer."
print(programming_dictionary)

for thing in programming_dictionary:
    print(thing)

for key in programming_dictionary:
    print(programming_dictionary[key])