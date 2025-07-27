from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Shahin's snake game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

food = Food()
scoreboard = Scoreboard()
my_snake = Snake()


screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    # Detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall.
    if (my_snake.head.xcor() > 280 or my_snake.head.xcor() < -300 or my_snake.head.ycor() > 300 or
            my_snake.head.ycor() < -280):
        scoreboard.reset()
        my_snake.reset()
    for segment in my_snake.segment_list[1:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard.reset()
            my_snake.reset()


screen.exitonclick()




