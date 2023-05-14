from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
X_CORD = 350
N_OF_CARS = 50


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = [Car() for _ in range(N_OF_CARS)]

    def move_cars(self):
        """Moves cars forward"""
        for car in self.cars:
            car.forward(self.speed)

    def cars_go_again(self):
        """If a cars goes beyond -X_CORD, its position is reset to (X_CORD,randomized_y)"""
        for car in self.cars:
            if car.xcor() < -X_CORD:
                car.setpos((-car.xcor(), randint(-235, 250)))
                car.color(choice(COLORS))

    def level_achieved(self):
        """Increases the speed of the cars and places them randomly across the screen"""
        self.speed += MOVE_INCREMENT
        for car in self.cars:
            car.goto(randomize_cords())


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.penup()
        self.shapesize(1, 1.5, 1)
        self.goto(randomize_cords())
        self.setheading(180)


def randomize_cords():
    """Returns a tuple of randomized (x,y) coordinates"""
    x = randint(-X_CORD, X_CORD)
    y = randint(-235, 250)
    return x, y
