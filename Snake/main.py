from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Scoreboard


screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

scoreboard=Scoreboard()
snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")


game_on=True
while game_on:
    screen.update( )
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) <15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.snake_head.xcor() >280 or snake.snake_head.xcor() <-280 or snake.snake_head.ycor()>280 or snake.snake_head.ycor()<-280 :
        snake.reset()
        scoreboard.reset_score()
    for segment in snake.snake_seg[1:] :
        if snake.snake_head.distance(segment) <10 :
            snake.reset()
            scoreboard.reset_score( )
screen.exitonclick()