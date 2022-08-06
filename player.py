from turtle import Turtle
X_START_POSITION = 0
Y_START_POSITION = -285


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=X_START_POSITION, y=Y_START_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def new_game(self):
        self.goto(x=X_START_POSITION, y=Y_START_POSITION)

