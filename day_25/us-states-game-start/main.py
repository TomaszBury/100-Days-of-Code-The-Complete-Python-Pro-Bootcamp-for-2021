from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

with open("50_states.csv") as data:
    states = data.readlines()

game_is_on = 5

while game_is_on >= 0:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    # print(answer_state)

    for state in states:
        # print(state.strip())
        # print(type(state))
        # print(state.split(",")[0])
        if state.split(",")[0].lower() == str(answer_state).strip().lower():
            # print(state[len(answer_state)+1::])
            x_cor = int(state.split(",")[1].strip())
            y_cor = int(state.split(",")[2].strip())
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.goto(x_cor, y_cor)
            new_turtle.write(state.split(",")[0])

    game_is_on -= 1

screen.exitonclick()
