def my_function(something):
    #Do this with something
    #Then do this 
    #Finally do this
    result = 3 + 2 - something
    return result

print(my_function(0))

def format_name(name):
    return name.upper()

print(format_name("Son"))

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    first_name = f_name.title()
    last_name = l_name.title()
    print(f"{first_name}:{last_name}")
    return f"{first_name} : {last_name}"

format_name("angela","Merkel")
print(format_name("wefg","ghent"))
print(format_name(input("What is your first name:"),input("What is your last name:")))