"""
The ScoreBoard class for the Pong Game. Handles score tracking and display.
"""

from turtle import Turtle

class ScoreBoard(Turtle):
    """
    A class to represent the scoreboard in the Pong game.
    """

    def __init__(self):
        """
        Initializes the scoreboard with zero points for both players.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_points = 0
        self.l_points = 0
        self.update_score_board()

    def update_score_board(self):
        """
        Clears the previous score and writes the current score on the screen.
        """
        self.clear()
        self.goto(x=100, y=220)
        self.write(self.r_points, False, "center", ("courier", 50, "normal"))
        self.goto(x=-100, y=220)
        self.write(self.l_points, False, "center", ("courier", 50, "normal"))

    def add_r_points(self):
        """
        Increments the right player's score and updates the display.
        """
        self.r_points += 1
        self.update_score_board()

    def add_l_points(self):
        """
        Increments the left player's score and updates the display.
        """
        self.l_points += 1
        self.update_score_board()

    def r_win(self):
        """
        Displays the 'GAME OVER' message and declares the right player as the winner.
        """
        self.goto(0, 0)
        self.write("GAME OVER\nR User Wins", False, "center", ("courier", 50, "normal"))

    def l_win(self):
        """
        Displays the 'GAME OVER' message and declares the left player as the winner.
        """
        self.goto(0, 0)
        self.write("GAME OVER\nL User Wins", False, "center", ("courier", 50, "normal"))
