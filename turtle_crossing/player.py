from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    """A class to manage the player's turtle and movement."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.start_position()
        self.setheading(90)

    def start_position(self):
        """Moves the turtle to its starting position."""
        self.goto(STARTING_POSITION)

    def move_forward(self):
        """Moves the turtle forward by a set distance."""
        self.forward(MOVE_DISTANCE)
