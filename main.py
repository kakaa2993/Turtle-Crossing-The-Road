from turtle import Screen
from player import Player
from cars_generated import Cars
import time
from scoreboard import Scoreboard
MOVEMENT_DISTANCE = 10

screen = Screen()
screen.title("Turtle Crossing The Road")
screen.tracer(0)
screen.bgcolor("white")
screen.setup(width=600, height=600)

player = Player()
scoreboard = Scoreboard()
screen.colormode(255)
screen.listen()
screen.onkey(key='Up', fun=player.move_up)
cars = Cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a random car every 0.1 second
    cars.create_a_car()

    # Move all the cars with a distance
    cars.move(movement_distance=MOVEMENT_DISTANCE)

    # Detect the collision with the cars
    if player.ycor() > 280:
        player.new_game()
        MOVEMENT_DISTANCE += 5
        scoreboard.upgrade_level()
    # if the car is reached the end of screen restart the position
    for car in cars.all_cars:
        # Detect the collision with the cars
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.lose_the_game()
            break
        # if the car pass the screen then delete it from the cars list
        if car.xcor() < -310:
            cars.all_cars.remove(car)

screen.exitonclick()