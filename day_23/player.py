from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.step = 20
        self.go_to_start()
        self.left(90)

    def go_up(self):
        if self.ycor() < 300:
            self.forward(MOVE_DISTANCE)
        # if self.ycor() < 280:
        #     new_y = self.ycor() + 20
        #     self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > - 300:
            self.backward(MOVE_DISTANCE)
            # new_y = self.ycor() - 20
            # self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
