from turtle import Turtle
FONT = ("Courier", 24, "normal")
TEXT_POSITION = (-200, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.level = 0
        self.color("black")
        self.goto(TEXT_POSITION)
        self.write_level()

    def write_level(self):
        """Writing Level: {lvl}"""
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        """Increasing the level on the scoreboard"""
        self.level += 1
        self.clear()
        self.write_level()


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()

    def write_game_over(self):
        """Writing 'Game over' in the middle of the screen"""
        self.write("Game over", align="center", font=("Courier", 24, "bold"))
