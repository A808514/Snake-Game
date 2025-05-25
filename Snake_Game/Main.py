from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import Board
import time

window = Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=800, height=800)
window.tracer(0)

sam = Snake()
food = Food()
score_board = Board()

window.update()

game_on = True
while game_on:
    sam.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(sam.up, "Up")
    window.onkey(sam.down, "Down")
    window.onkey(sam.right, "Right")
    window.onkey(sam.left, "Left")
    if sam.head.distance(food) < 15:
        food.appear()
        sam.extend()
        score_board.add_score()

    if (
        sam.head.xcor() > 375
        or sam.head.ycor() > 375
        or sam.head.xcor() < -375
        or sam.head.ycor() < -375
    ):
        game_on = False
        score_board.game_over()

    for segment in sam.body[0:-1]:
        if sam.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()


window.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import Board
import time

window = Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=800, height=800)
window.tracer(0)

sam = Snake()
food = Food()
score_board = Board()

window.update()

game_on = True
while game_on:
    sam.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(sam.up, "Up")
    window.onkey(sam.down, "Down")
    window.onkey(sam.right, "Right")
    window.onkey(sam.left, "Left")
    if sam.head.distance(food) < 15:
        food.appear()
        sam.extend()
        score_board.add_score()

    if (
        sam.head.xcor() > 375
        or sam.head.ycor() > 375
        or sam.head.xcor() < -375
        or sam.head.ycor() < -375
    ):
        game_on = False
        score_board.game_over()

    for segment in sam.body[0:-1]:
        if sam.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()


window.exitonclick()
