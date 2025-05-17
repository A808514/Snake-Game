from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        self.positions = [(-40, 0), (-20, 0), (0, 0), (20, 0), (40, 0), (60, 0)]
        self.angles = (90, 0, 0, 0)
        self.create_snake()
        self.head = self.body[-1]

    def create_snake(self):
        for i in range(len(self.positions)):
            new_turtule = Turtle("square")
            new_turtule.color("white")
            new_turtule.penup()
            new_turtule.goto(self.positions[i])
            self.body.append(new_turtule)

    def move(self):
        for i in range(len(self.body) - 1):
            self.body[i].goto(self.body[i + 1].pos())
        self.body[-1].fd(20)

    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.body[0].pos())
        self.body.insert(0, new_segment)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)
