from turtle import Turtle
import random
import time

random.seed(time.time())


class Cars(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(self.random_colors())
        self.setheading(180)
        self.goto(x=x_position, y=y_position)


    def random_colors(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return red, green, blue

    def move(self, movement_distance):
        self.forward(movement_distance)
        # self.goto(x=self.xcor() - movement_distance, y=self.ycor())

    def restart(self, position):
        self.goto(position)
        # x = random.randrange(300, 900, step=50), y = random.randrange(-240, 230, step=40)





