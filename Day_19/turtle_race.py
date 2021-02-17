from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Chose winner color: ")

tim = Turtle(shape="turtle")
tim.penup()
tim.goto(x = -230, y = -180)
print(tim.position())
#print(tim.distance(x= 100))





screen.exitonclick()
