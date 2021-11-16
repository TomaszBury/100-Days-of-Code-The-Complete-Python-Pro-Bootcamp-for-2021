from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white',
                                 padx=20, pady=20, font=('Arial', 12, 'italic'))
        self.score_label.grid(column=1, row=0, sticky=E)
        self.canvas = Canvas(width=300, height=250)

        self.question_text = self.canvas.create_text(150, 125,
                                                     text="test test test test test test test test test test test test test test test test test test test test test ",
                                                     width=300,
                                                     font=('Arial', 20, 'italic'))
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.window.mainloop()
