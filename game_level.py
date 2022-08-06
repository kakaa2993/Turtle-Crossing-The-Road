from turtle import Turtle
FONT = ('Fantasy', 24, 'normal')


class GameLevel(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("Black")
        self.level = 1
        self.hideturtle()
        self.goto(x=-210,y=260)
        self.write(f"Level: {self.level}", align="center",  font=FONT)
        self.movement_distance = 1

    def upgrade_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center",  font=FONT)

    def lose_the_game(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center",  font=FONT)

    def increase_speed(self):
        self.movement_distance += 1

