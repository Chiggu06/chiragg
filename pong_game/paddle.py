"""
The Paddle class for the Pong Game. Handles paddle movement and positioning.
"""

from turtle import Turtle

class Paddle(Turtle):
    """
    A class to represent a paddle in the Pong game.
    """

    def __init__(self, position):
        """
        Initializes the paddle at a given position.
        :param position: A tuple (x, y) representing the starting position.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        """
        Moves the paddle up by 20 units if it's within the top boundary.
        """
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        """
        Moves the paddle down by 20 units if it's within the bottom boundary.
        """
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
