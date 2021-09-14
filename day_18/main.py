from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.color("brown")
# https://cs111.wellesley.edu/labs/lab01/colors
# https://docs.python.org/3/library/turtle.html
# https://trinket.io/docs/colors
timmy_the_turtle.forward(100)
timmy_the_turtle.color("peru")
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.color("yellow")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.color("lime green")

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

timmy_the_turtle.color("pale violet red")
for _ in range(4):
    timmy_the_turtle.forward(200)
    timmy_the_turtle.right(90)

timmy_the_turtle.color("medium violet red")
timmy_the_turtle.left(90)
for _ in range(4):
    timmy_the_turtle.forward(200)
    timmy_the_turtle.left(90)

timmy_the_turtle.color("dark magenta")
timmy_the_turtle.forward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(200)
for _ in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(400)

timmy_the_turtle.right(135)
diagonal = 400 * (2 ** 0.5)
timmy_the_turtle.forward(diagonal)
timmy_the_turtle.left(135)
timmy_the_turtle.color("green yellow")
timmy_the_turtle.forward(200)

timmy_the_turtle.left(45)
diagonal = 200 * (2 ** 0.5)

for _ in range(4):
    timmy_the_turtle.forward(diagonal)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()

