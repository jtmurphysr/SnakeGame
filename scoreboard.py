from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Do not draw while moving
        self.goto(0, 370)  # Position the scoreboard at the top of the screen
        self.color("white")  # Set text color to white
        self.score = 0  # Initialize the score as 0
        # Write the initial score to the screen
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        # Display "Game Over" message at the center of the screen
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        # Increment the current score and update the scoreboard
        self.score += 1  # Add 1 to the score
        self.clear()  # Clear the previous score display
        # Rewrite the updated score
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
