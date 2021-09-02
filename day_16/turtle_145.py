# import turtle
from turtle import Turtle, Screen


import anotyher_module

print(anotyher_module.another_variable)

# timmy = turtle.Turtle()
timmy = Turtle()


print(timmy)
timmy.shape("turtle")
timmy.color('DarkOrchid3')
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)

my_screen = Screen()

print(my_screen.canvheight)
print(my_screen.canvwidth)

my_screen.exitonclick()
