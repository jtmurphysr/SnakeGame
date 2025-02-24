from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set food shape
        self.penup()  # Disable drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Resize the food (small circle)
        self.color("blue")  # Set food color
        # Place food in a random position initially
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        # Move food to a new random position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
