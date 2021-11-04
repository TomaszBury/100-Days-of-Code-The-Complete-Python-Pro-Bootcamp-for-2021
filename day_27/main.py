from tkinter import *

window = Tk()
window.title("My first GIU Program")
window.minsize(width=500, height=300)

# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# Label
my_label = Label(text="I am a Label.", font=("Arial", 24, "italic"))
my_label.pack(side="left")

my_label["text"] = "New text"
my_label.config(text="New New text")


# Button
def button_clicked():
    my_label.config(text="Button got clicked.")
    my_label.config(text=input_on_window.get())
    print("I got clicked")


button = Button(text="Click Me.", command=button_clicked)
button.pack(side="right")


# Entry
input_on_window = Entry(width=10)
input_on_window.pack()


# The very last thing:
window.mainloop()
