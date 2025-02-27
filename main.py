from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

BOUNDARY = 380
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
turtle_width = 20
my_score = Scoreboard()


#Add turtle
#TODO input variable of current snake position as x and y values
snake = Snake(0,0)
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        my_score.increase_score()
        snake.add_segment()

    #Detect collision with wall
    if snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY or snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY:
        game_is_on = False
        my_score.game_over()

    #Detect collision with tail
    #If head collides with any segment of snake, trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            my_score.game_over()
            break

screen.exitonclick()
