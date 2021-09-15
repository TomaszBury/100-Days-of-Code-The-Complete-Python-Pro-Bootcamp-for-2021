from turtle import Turtle, Screen

tim = Turtle()
tim.color("brown")
# https://cs111.wellesley.edu/labs/lab01/colors
# https://docs.python.org/3/library/turtle.html
# https://trinket.io/docs/colors
tim.forward(100)
tim.color("peru")
tim.right(90)
tim.forward(100)
tim.right(90)
tim.color("yellow")
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.color("lime green")

for _ in range(4):
    tim.forward(100)
    tim.left(90)

tim.color("pale violet red")
for _ in range(4):
    tim.forward(200)
    tim.right(90)

tim.color("medium violet red")
tim.left(90)
for _ in range(4):
    tim.forward(200)
    tim.left(90)

tim.color("dark magenta")
tim.forward(200)
tim.right(90)
tim.forward(200)
for _ in range(4):
    tim.right(90)
    tim.forward(400)

tim.right(135)
diagonal = 400 * (2 ** 0.5)
tim.forward(diagonal)
tim.left(135)
tim.color("green yellow")
tim.forward(200)

tim.left(45)
diagonal = 200 * (2 ** 0.5)

for _ in range(4):
    tim.forward(diagonal)
    tim.left(90)

screen = Screen()
screen.exitonclick()

