from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)
my_label.config(padx=5, pady=5)

my_label = Label(text="is equal to:")
my_label.grid(column=0, row=1)
my_label.config(padx=5, pady=5)

Label_value = Label(text="0")
Label_value.grid(column=1, row=1)
Label_value.config(padx=5, pady=5)

my_label = Label(text="Km")
my_label.grid(column=2, row=1)
my_label.config(padx=5, pady=5)


def miles_to_km():
    if miles_input.get() == "":
        Label_value.config(text="Please input value first.")
    else:
        km = f"{float(miles_input.get()) * 1.609344:.2f}"
        Label_value.config(text=km)


button = Button(text="Click Me.", command=miles_to_km)
button.grid(column=1, row=2)

# The very last thing:
window.mainloop()
