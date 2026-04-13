from turtle import Turtle

class ScoreBoard(Turtle):
    """A class to handle the score and high score display and persistence."""

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                self.highscore = int(data.read())
        except FileNotFoundError:
            self.highscore = 0
            with open("data.txt", "w") as data:
                data.write("0")

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.count()

    def count(self):
        """Displays the current score and the high score."""
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, "center", ("courier", 20, "normal"))

    def update_score(self):
        """Clears the current display and refreshes it with the latest score."""
        self.clear()
        self.count()

    def increase_score(self):
        """Increments the current score and updates the display."""
        self.score += 1
        self.update_score()

    def reset(self):
        """Checks for a new high score, persists it if found, and resets current score."""
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
