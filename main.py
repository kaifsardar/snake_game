import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.head.distance(food)<15:
        score.increse_score()
        snake.extend()
        food.refresh()
    
    #checking if collide with walls
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.game_over()
        game_is_on=False
    
    #checking if head is touching any part of the snake or not

    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10 :
            game_is_on=False
            score.game_over()


screen.exitonclick()