from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(10)


def turn():
    tom.setheading(5)


# https://docs.python.org/3/library/turtle.html#turtle.listen
screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()
