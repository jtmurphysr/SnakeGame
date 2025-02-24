from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set the boundary for the game area
BOUNDARY = 380

# Set up the game screen
screen = Screen()
screen.setup(width=800, height=800)  # Game screen size
screen.bgcolor("black")  # Background color of the game
screen.title("Snake Game")  # Game window title
screen.tracer(0)  # Turn off animation for smooth screen updates
turtle_width = 20  # Width of a single snake segment

# Create an instance of Scoreboard class to display scores
my_score = Scoreboard()

# Create the initial snake object and food object
snake = Snake(0, 0)  # Snake starts at position (0, 0)
food = Food()  # Create the food object

# Enable key listeners to control snake movement
screen.listen()
screen.onkey(snake.up, "Up")  # Move Up
screen.onkey(snake.down, "Down")  # Move Down
screen.onkey(snake.left, "Left")  # Move Left
screen.onkey(snake.right, "Right")  # Move Right

# Variable to control the game loop
game_is_on = True

# Main game loop
while game_is_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Add delay for smoother movement
    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:  # If the snake's head is close enough to the food
        food.refresh()  # Move the food to a new position
        my_score.increase_score()  # Increase the score
        snake.add_segment()  # Add a new segment to the snake

    # Detect collision with the wall
    if (snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY or
            snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY):
        game_is_on = False  # End the game
        my_score.game_over()  # Display "Game Over"

    # Detect collision with the tail
    for segment in snake.segments[1:]:  # Exclude the head from the check
        if snake.head.distance(segment) < 10:  # If head collides with any segment
            game_is_on = False  # End the game
            my_score.game_over()  # Display "Game Over"
            break

# Close the game screen upon exit
screen.exitonclick()