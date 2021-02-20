#Version 2 using dictionary
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Chose winner color: ")

is_run = True
#Tim
tim = Turtle(shape="turtle")
tim.penup()
tim.color("red")
tim.goto(x = -230, y = -180)

#Bob
bob = Turtle(shape="turtle")
bob.penup()
bob.color("pink")
bob.goto(x = -230, y = -150)

#Jack
jack= Turtle(shape="turtle")
jack.penup()
jack.color("green")
jack.goto(x = -230, y = -120)

#Ron
ron= Turtle(shape="turtle")
ron.penup()
ron.color("blue")
ron.goto(x = -230, y = -90)

#Deb
deb= Turtle(shape="turtle")
deb.penup()
deb.goto(x = -230, y = -60)

turtles = {tim: "red", bob: "pink", jack: "green", ron: "blue", deb: "black",}


def run(name):
    x_pos = name.position()
    if x_pos[0] <= 220:
        name.forward(randint(1, 20))
        return True
    else:
        decide_winner(name)
        return False


def decide_winner(turtle_name):
    winner_color = turtles[turtle_name]
    if winner_color == user_bet:
        print(f"You WINNER! {winner_color.title()} is first turtle!")        
    else:
        print(f"You LOSER! {winner_color.title()} is first turtle!")


while is_run:
    for turtle in turtles:
        if is_run:
            is_run = run(turtle)
        else:
            break

screen.exitonclick()
