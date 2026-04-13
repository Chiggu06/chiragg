"""
The Ball class for the Pong Game. Handles ball movement, bouncing, and speed.
"""

from turtle import Turtle

class Ball(Turtle):
    """
    A class to represent the ball in the Pong game.
    """

    def __init__(self):
        """
        Initializes the ball at the center with initial movement and speed.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """
        Moves the ball based on its current x and y movement values.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        """
        Reverses the ball's y-direction when it hits the top or bottom wall.
        """
        self.y_move *= -1

    def change_direction(self):
        """
        Reverses the ball's x-direction and increases its speed when it hits a paddle.
        """
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """
        Resets the ball to the center, resets speed, and changes its x-direction.
        """
        self.home()
        self.ball_speed = 0.1
        self.change_direction()
