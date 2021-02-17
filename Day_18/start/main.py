#27min
from turtle import Turtle, Screen
from random import randint
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

def random_color_generator():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    return r, g, b

screen = Screen()
screen.colormode(255)

sides = 3
for shape in range(7):    
    angle = 360 / sides
    timmy_the_turtle.pencolor(random_color_generator())   
    for turn in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
    sides += 1










screen.exitonclick()