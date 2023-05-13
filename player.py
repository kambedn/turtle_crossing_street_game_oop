from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.reset_position()
        self.shape("turtle")

    def move(self):
        """Moves the turtle by MOVE_DISTANCE forward"""
        self.forward(MOVE_DISTANCE)

    def finish(self):
        """Returns True if the player finished a level"""
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        """Moves the turtle to the starting position"""
        self.goto(STARTING_POSITION)