"""
The main entry point for the Pong Game. Handles the game loop and screen updates.
"""

from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

def main():
    """
    Main function to initialize and run the Pong game.
    """
    screen = Screen()
    screen.setup(height=600, width=800)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    game_over = False

    scoreboard = ScoreBoard()
    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0))
    ball = Ball()

    screen.listen()
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")

    while not game_over:
        screen.update()
        time.sleep(ball.ball_speed)
        ball.move()

        # Wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()

        # Paddle collision
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
            ball.change_direction()

        if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.change_direction()

        # r_paddle_miss
        if ball.xcor() > 380:
            scoreboard.add_l_points()
            ball.reset_position()

        # l_paddle_miss
        if ball.xcor() < -380:
            scoreboard.add_r_points()
            ball.reset_position()

        # Check for winner
        if scoreboard.r_points == 15:
            scoreboard.r_win()
            game_over = True
        elif scoreboard.l_points == 15:
            scoreboard.l_win()
            game_over = True

    screen.exitonclick()

if __name__ == "__main__":
    main()
