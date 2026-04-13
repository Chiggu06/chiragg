from turtle import Turtle


class LevelCard(Turtle):
    """A class to manage and display the game level and game over message."""

    def __init__(self):
        super().__init__()
        self.start_lev = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_level()

    def update_level(self):
        """Displays the current level on the screen."""
        self.clear()
        self.goto(-320, 260)
        self.write(f"Level: {self.start_lev}", False, "center", ("courier", 20, "normal"))

    def increase_level(self):
        """Increments the level and updates the display."""
        self.start_lev += 1
        self.update_level()

    def game_over(self):
        """Displays the 'GAME OVER' message in the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("courier", 80, "bold"))
