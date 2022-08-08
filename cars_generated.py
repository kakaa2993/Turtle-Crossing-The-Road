from turtle import Turtle
import random
import time

random.seed(time.time())


class Cars:

    def __init__(self):
        self.all_cars = []
        self.movement_distance = 10

    def random_colors(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return red, green, blue

    def move(self, movement_distance):
        for car in self.all_cars:
            car.backward(movement_distance)

    def create_a_car(self):
        random_choice = random.randint(1, 4)
        if random_choice == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(self.random_colors())
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)




