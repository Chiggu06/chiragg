from turtle import Turtle
import random

COLOURS = ["blue", "green", "pink", "yellow", "red", "orange", "purple"]


class Cars(Turtle):
    """A class to represent individual cars in the game."""

    def __init__(self):
        super().__init__()

    def cars_generation(self):
        """Initializes the car's appearance and starting position."""
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.color(random.choice(COLOURS))
        self.goto(400, random.randint(-250, 250))

    def move(self, speed):
        """Moves the car backward at the given speed."""
        self.backward(speed)
