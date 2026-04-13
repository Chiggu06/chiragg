from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A class to manage the snake's body and movement."""

    def __init__(self):
        self.segments = []
        self.snake_body()
        self.head = self.segments[0]

    def snake_body(self):
        """Initializes the snake's body with starting segments."""
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake's body."""
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        """Adds a new segment at the end of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward by following the segment in front of it."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        """Changes heading to Up if not currently moving Down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        """Changes heading to Down if not currently moving Up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        """Changes heading to Left if not currently moving Right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        """Changes heading to Right if not currently moving Left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """Resets the snake to its starting state."""
        for seg in self.segments:
            seg.goto(1000, 1000)
            seg.hideturtle()
        self.segments.clear()
        self.snake_body()
        self.head = self.segments[0]
