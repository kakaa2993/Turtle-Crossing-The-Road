from turtle import Turtle,Screen
from player import Player
from cars_generated import Cars
import time
import random
import itertools
from game_level import GameLevel
MOVEMENT_DISTANCE = 10

screen = Screen()
screen.title("Turtle Crossing The Road")
screen.tracer(0)
screen.bgcolor("white")
screen.setup(width=600, height=600)
player = Player()
level = GameLevel()
screen.colormode(255)
screen.listen()
screen.onkey(key='Up', fun=player.move_up)

game_is_on = True
while game_is_on:
    cycle = 0

    # Filter the position of the cars
    list_of_x = [x for x in range(300, 900, 50)]
    list_of_y = [x for x in range(-240, 230, 40)]
    list_of_taken_position = []

    # Create multiple cars inside a list
    cars_list = []
    for _ in range(50):
        random_x = random.choice(list_of_x)
        random_y = random.choice(list_of_y)
        position = (random_x, random_y)
        if position not in list_of_taken_position:
            list_of_taken_position.append(position)
            car = Cars(random_x, random_y)
            cars_list.append(car)

    # Add all the cars 10 distance
    for car in itertools.cycle(cars_list):
        # Detect the collision with the cars
        if car.distance(player) <= 30:
            game_is_on = False
            level.lose_the_game()
            break
        if player.ycor() > 280:
            player.new_game()
            MOVEMENT_DISTANCE += 5
        car.move(movement_distance=MOVEMENT_DISTANCE)
        # if the car is reached the end of screen restart the position
        if car.xcor() < -300:
            random_position = random.choice(list_of_taken_position)
            if (cars_list[cars_list.index(car) - 1].xcor(), cars_list[cars_list.index(car) - 1].ycor()) != random_position:
                car.restart(random_position)
            else:
                car.restart(random.choice(list_of_taken_position))
        cycle += 1
        if cycle > 10000:
            screen.update()











screen.exitonclick()