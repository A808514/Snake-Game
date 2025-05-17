from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.update_board()

    def update_board(self):
        self.write(
            f"Score: {self.score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.screen.bgcolor("dark red")
        self.goto(0, 0)
        self.write(
            f"Game Over!\nFinal Score: {self.score}",
            font=("Arial", 30, "normal"),
            align="center",
        )
