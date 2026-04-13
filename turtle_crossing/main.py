import time
import random
from turtle import Screen
from player import Player
from cars import Cars
from levelcard import LevelCard

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Game objects
turtle = Player()
level = LevelCard()

# Keyboard bindings
screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_is_on = True
all_cars = []
car_speed = 5

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate cars randomly
    if random.randint(1, 6) == 1:
        new_car = Cars()
        new_car.cars_generation()
        all_cars.append(new_car)

    # Move cars and check for collisions
    for car in all_cars:
        car.move(car_speed)

        # Collision detection
        if turtle.distance(car) < 25:
            level.game_over()
            game_is_on = False

    # Remove cars that go off-screen to improve performance
    all_cars = [car for car in all_cars if car.xcor() > -450]

    # Check for successful crossing
    if turtle.ycor() > 300:
        turtle.start_position()
        level.increase_level()
        car_speed += 2

screen.exitonclick()
