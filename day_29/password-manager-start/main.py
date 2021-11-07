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

    if len(address) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        web_address_input.focus()
    else:
        is_ok_to_save = messagebox.askokcancel(title=address,
                                               message=f"These are the details entered: \nEmail: {username} "
                                                       f"\nPassword: {user_password} \nIs it ok to save?")

        if is_ok_to_save:
            data_to_write = f"{address} | {username} | {user_password} \n"

            with open("data.txt", "a") as data:
                data.writelines(data_to_write)

            password_input.delete(0, END)
            web_address_input.delete(0, END)
            web_address_input.focus()
        else:
            web_address_input.focus()


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
web_address_input = Entry(width=55)
web_address_input.grid(column=1, row=1, columnspan=2)
web_address_input.focus()

username_input = Entry(width=55)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "fake_e-mail@fake.com")

password_input = Entry(width=36)
password_input.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", width=46, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
