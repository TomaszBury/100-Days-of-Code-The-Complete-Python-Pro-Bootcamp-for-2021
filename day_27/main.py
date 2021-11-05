from tkinter import *

window = Tk()
window.title("My first GIU Program")
window.minsize(width=500, height=300)

# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# Label
my_label = Label(text="I am a Label.", font=("Arial", 24, "italic"))
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New New text")


# Button
def button_clicked():
    my_label.config(text="Button got clicked.")
    my_label.config(text=input_on_window.get())
    print("I got clicked")


button = Button(text="Click Me.", command=button_clicked)
# button.pack(side="right")
button.grid(column=1, row=1)


# Entry
input_on_window = Entry(width=10)
# input_on_window.pack()
# cannot use geometry manager pack inside . which already has slaves managed by grid
input_on_window.grid(column=2, row=2)

# The very last thing:
window.mainloop()
