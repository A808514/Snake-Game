
# ( TURTLES RACE PROJECT_1)

# from turtle import Turtle , Screen
# import random

# distance = [10 , 20 , 30 , 40 , 50 ]
# sam1 = Turtle()
# sam2 = Turtle()
# sam3 = Turtle()
# window = Screen()
# window.setup(1000 , 700)
# # sam1
# sam1.color("green")
# sam1.shape("turtle")
# sam1.penup()
# sam1.goto(-450 , 300)
# # sam2
# sam2.color("red")
# sam2.shape("turtle")
# sam2.penup()
# sam2.goto(-450 , 0)
# # sam3
# sam3.color("blue")
# sam3.shape("turtle")
# sam3.penup()
# sam3.goto(-450 , -300)

# window.title("Turtles Race")
# massage = window.textinput("Make your bet" , "Guess the winner:\nTypr a color: Red, Blue or Green")

# for _ in range(29):
#     sam3.fd(random.choice(distance))
#     sam1.fd(random.choice(distance))
#     sam2.fd(random.choice(distance))

# if massage.lower() == "green" and sam1.xcor() >= 450 :
#     window.bgcolor("black")
#     sam1.hideturtle()
#     sam1.goto(0 , 0)
#     sam1.write("You Win 🤩" , font= ("arial", 40, "normal") , align= "center" )
# elif massage.lower() == "green" and sam1.xcor() < 450 :
#     window.bgcolor("black")
#     sam1.hideturtle()
#     sam1.goto(0 , 0)
#     sam1.write("You Lose 😢" , font= ("arial", 40, "normal") , align= "center" )

# elif massage.lower() == "red" and sam2.xcor() >= 450 :
#     window.bgcolor("black")
#     sam2.hideturtle()
#     sam2.goto(0 , 0)
#     sam2.write("You Win 🤩" , font= ("arial", 40, "normal") , align= "center" )
# elif massage.lower() == "red" and sam2.xcor() < 450 :
#     window.bgcolor("black")
#     sam2.hideturtle()
#     sam2.goto(0 , 0)
#     sam2.write("You Lose 😢" , font= ("arial", 40, "normal") , align= "center" )

# elif massage.lower() == "blue" and sam3.xcor() >= 450 :
#     window.bgcolor("black")
#     sam3.hideturtle()
#     sam3.goto(0 , 0)
#     sam3.write("You Win 🤩" , font= ("arial", 40, "normal") , align= "center" )
# elif massage.lower() == "blue" and sam3.xcor() < 450:
#     window.bgcolor("black")
#     sam3.hideturtle()
#     sam3.goto(0 , 0)
#     sam3.write("You Lose 😢", font= ("arial", 40, "normal") , align= "center" )

# window.exitonclick()

# ------------------------------------------------------------------------------------------------

# ( TURTLES RACE PROJECT_2)

from turtle import Turtle , Screen
import random

window = Screen()
window.title("TURTLES RACE")
window.setup(width=600 , height=400)
colors = ("red", "blue", "green")
y_positions = (-70, 0 ,70)

turtles = []
user_bet = window.textinput(title="Make your bet", prompt="Guess the winner:\nType a color: Red, Blue or Green")

for i in range(3):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-280 , y= y_positions[i])
    turtles.append(new_turtle)

def race_turtle():
    is_race_on = True
    while is_race_on :
        for turtle in turtles:
            if turtle.xcor() > 280 :
                is_race_on = False
                winning_color = turtle.pencolor()
                display_result(winning_color == user_bet)
            else :
                turtle.fd(random.randint(1,5))

def display_result(is_winner):
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0,0)
    result_turtle.pendown()

    if is_winner :
        window.bgcolor("dark green")
        result_turtle.color("white")
        result_turtle.write("You Win!", align= "center", font= ("Arial",28, "normal"))
    else:
        window.bgcolor("medium violet red")
        result_turtle.color("white")
        result_turtle.write("You Lose!", align= "center", font=("Arial",28, "normal"))

race_turtle()

window.exitonclick()
