from tkinter import *

window = Tk()
window.title("My first GIU Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a Label.", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)
my_label.config(padx=15, pady=15)


def button_clicked():
    if input_on_window.get() != "":
        my_label.config(text=input_on_window.get())
    else:
        my_label.config(text="I got clicked")


def new_button_clicked():
    my_label.config(text="I got clicked by new button.")


button = Button(text="Click Me.", command=button_clicked)
button.grid(column=1, row=1)

second_button = Button(text="New Button", command=new_button_clicked)
second_button.grid(column=2, row=0)

input_on_window = Entry(width=10)
input_on_window.grid(column=3, row=2)

# The very last thing:
window.mainloop()
