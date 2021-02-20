#Generating turtles
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
colors = ["red", "pink", "green", "blue", "yellow"]
user_bet = screen.textinput(title= "Make your bet", prompt= "Chose winner color: ").lower()
y_pos = -180 #y position for first Turtle
turtles = []

is_run = True
for color in colors:
    y_pos += 30
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color) 
    new_turtle.goto(x = -230, y = y_pos)
    turtles.append(new_turtle)


def run(name):
    x_pos = name.position()
    if x_pos[0] <= 220:
        name.forward(randint(1, 20))
        return True
    else:
        decide_winner(name)
        return False


def decide_winner(turtle_name):
    winner_color = turtle_name.color()[1]
    if winner_color == user_bet:
        print(f"You WINNER! {winner_color.title()} is first turtle!")        
    else:
        print(f"You LOSER! {winner_color.turtle()} is first turtle!")


while is_run:
    for turtle in turtles:
        if is_run:
            is_run = run(turtle)
        else:
            break

screen.exitonclick()
