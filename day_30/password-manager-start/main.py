import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = ''.join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    address = web_address_input.get()
    username = username_input.get()
    user_password = password_input.get()
    new_data = {
        address: {
            "email": username,
            "password": user_password,
        }
    }

    if len(address) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        web_address_input.focus()
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        password_input.delete(0, END)
        web_address_input.delete(0, END)
        web_address_input.focus()


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        user_name = data[web_address_input.get()]['email']
        user_password = data[web_address_input.get()]['password']
    except FileNotFoundError:
        messagebox.showerror('Error', 'Database is empty!')
    except KeyError:
        messagebox.showerror("Error", "No details for the website exists.")
    else:
        messagebox.showinfo(title="Password",
                            message=f"E-mail / User name: {user_name}\n"
                                    f"Your Password: {user_password}")
        pyperclip.copy(user_password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_logo)
canvas.grid(column=1, row=0)

# Labels
web_address_label = Label(text="Website:")
web_address_label.grid(column=0, row=1, sticky=E)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, sticky=E)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=E)

# Entries
web_address_input = Entry(width=36)
web_address_input.grid(column=1, row=1, columnspan=1)
web_address_input.focus()

username_input = Entry(width=55)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "fake_e-mail@fake.com")

password_input = Entry(width=36)
password_input.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Search", width=15, command=find_password)
generate_password_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", width=46, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
