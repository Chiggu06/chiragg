"""
The main entry point for the Snake Game. Handles the game loop and screen updates.
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

def main():
    """Starts the Snake Game."""
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(600, 600)
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")

    game_over = False

    while not game_over:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.generate_food()
            scoreboard.increase_score()
            snake.grow()

        # Detect collision with wall
        if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            scoreboard.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

    screen.exitonclick()

if __name__ == "__main__":
    main()
