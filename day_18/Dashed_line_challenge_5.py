from turtle import Turtle, Screen

tom = Turtle()
tom.left(180)
tom.penup()
tom.forward(15*30)
tom.right(180)

for _ in range(41):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen = Screen()
screen.exitonclick()
