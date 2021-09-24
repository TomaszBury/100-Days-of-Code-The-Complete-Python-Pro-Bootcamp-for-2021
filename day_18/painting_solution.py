# import colorgram
import turtle as turtle_modudle
import random

turtle_modudle.colormode(255)
tim = turtle_modudle.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

# rgb_colors = []
# colors = colorgram.extract('danmien_hirst_complete_sport.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

color_list = [(205, 155, 102), (54, 97, 138), (141, 160, 190), (146, 86, 57), (197, 143, 167), (22, 44, 58), (232, 208, 107), (144, 69, 93), (177, 156, 47), (63, 120, 85), (193, 87, 121), (205, 89, 66), (138, 175, 154), (224, 170, 189), (61, 43, 33), (103, 120, 168), (13, 57, 46), (180, 186, 213), (9, 98, 72), (44, 58, 101), (56, 34, 41), (87, 155, 106), (229, 174, 164), (99, 45, 62), (228, 207, 13), (108, 44, 38)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim. forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_modudle.Screen()
screen.exitonclick()

