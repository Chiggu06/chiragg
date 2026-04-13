from turtle import Turtle
import random

class Food(Turtle):
    """A class to represent the food in the Snake Game."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.penup()
        self.generate_food()

    def generate_food(self):
        """Moves the food to a random position on the screen."""
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.goto(rand_x, rand_y)
