from turtle import Turtle


class Bowl(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 6)
        self.goto(0, -360)

    def move_right(self):
        new_x = self.xcor() + 50
        if new_x < 450:
            self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 50
        if new_x > -450:
            self.goto(new_x, self.ycor())