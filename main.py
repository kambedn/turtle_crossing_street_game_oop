import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Help the turtle cross the road!")
screen.tracer(0)

# Creating a turtle
turtle = Player()

# Creating a scoreboard
scoreboard = Scoreboard()

# Creating a car manager, whose cars attribute stores cars
car_manager = CarManager()

# Creating a GameOver object, which shows up if the player loses
game_over = GameOver()

# If player presses the "Up" key, the turtle moves
screen.listen()
screen.onkeypress(turtle.move, "Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()
    car_manager.cars_go_again()

    # detecting if the player finished a level
    if turtle.finish():
        time.sleep(1)  # a short break
        turtle.reset_position()  # moving the turtle back to starting position
        scoreboard.update_level()  # updating scoreboard
        car_manager.level_achieved()  # increasing the speed of cars and locating them randomly

    # detecting if the turtle collided with a car
    for car in car_manager.cars:
        if turtle.distance(car) <= 20 and abs(turtle.xcor() - car.xcor()) < 9:
            game_is_on = False
            game_over.write_game_over()

print("RIP Timmy the Turtle")
screen.exitonclick()
