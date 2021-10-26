from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-258, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -280:
                car.hideturtle()
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


        # super().__init__()
        # self.color(random.choice(COLORS))
        # self.penup()
        # self.shape("square")
        # self.shapesize(stretch_wid=.5, stretch_len=2)
        # self.goto(position)

    # def go_left(self):
    #     if self.xcor() < 280:
    #         new_x = self.xcor() + MOVE_INCREMENT
    #         self.goto(new_x, self.ycor())
    #         return True
    #     else:
    #         return False
    #
    # def go_right(self):
    #     if self.xcor() > -280:
    #         new_x = self.xcor() - MOVE_INCREMENT
    #         self.goto(new_x, self.ycor())
    #         return False
    #     else:
    #         return True
