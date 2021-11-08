# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    print("There was an error.")
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"KeyError HaHaHa - That key:{error_message} does not exist.")
else:
    print("Great Success.")
    content = file.read()
    print(content)
finally:
    # file.close()
    # print("File was closed.")
    raise TypeError("※\\(^o^)/※This is an error that i made up.※\\(^o^)/※")

# KeyError: 'not_existent_key'
# a_dictionary = {"key": "value"}
#
# value = a_dictionary["not_existent_key"]

# IndexError: list index out of range
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError: can only concatenate str (not "int") to str
# text = 'abc'
# print(text + 5)
