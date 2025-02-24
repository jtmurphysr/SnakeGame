from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial snake's body positions
SNAKE_WIDTH = 20  # Width of each snake segment
MOVE_DISTANCE = 20  # Distance to move each step
UP = 90  # Upward direction (degrees)
DOWN = 270  # Downward direction (degrees)
LEFT = 180  # Left direction (degrees)
RIGHT = 0  # Right direction (degrees)


class Snake:
    def __init__(self, x, y):
        # Initialize the starting position of the snake
        self.x = x
        self.y = y
        self.segments = []  # List to hold the snake's segments
        self.create_snake(x, y)  # Create the initial snake body
        self.head = self.segments[0]  # Head of the snake
        self.tail = self.segments[-1]  # Tail of the snake

    def create_snake(self, x_pos, y_pos):
        # Create three initial segments of the snake
        for i in range(3):
            new_snake = Turtle()  # Create a new turtle instance
            new_snake.shape("square")  # Set shape to square
            new_snake.color("white")  # Set color to white
            new_snake.penup()  # Disable drawing while moving
            new_snake.speed(1)  # Set the speed to '1' (slow)
            # Position each segment adjacent to the previous one
            new_snake.goto(x=x_pos - (len(self.segments) * SNAKE_WIDTH), y=y_pos)
            self.segments.append(new_snake)  # Add the new segment to the list

    def add_segment(self):
        # Add a new segment to the snake at the position of the tail
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)
        new_segment.goto(x=self.tail.xcor(), y=self.tail.ycor())

    def move(self):
        # Move each segment to the position of the segment in front
        for snake_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_number - 1].xcor()
            new_y = self.segments[snake_number - 1].ycor()
            self.segments[snake_number].goto(x=new_x, y=new_y)
        # Move the head forward
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        # Turn left if not already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Turn right if not already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        # Turn up if not already moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Turn down if not already moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
