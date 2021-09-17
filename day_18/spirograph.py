import random
from turtle import Turtle, Screen
from random import Random

tom = Turtle()
tom.speed("fastest")
screen = Screen()
screen.colormode(255)


def random_color():
    return random.randrange(0, 255, 10), random.randrange(0, 255, 10), random.randrange(0, 255, 10)


def draw_spirograph(size_of_gap):
    how_many_circles = int(360 / size_of_gap)
    for _ in range(how_many_circles):
        tom.circle(100)
        # tom.left(10)
        tom.color(random_color())
        tom.setheading(tom.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
