from turtle import Turtle
from scoreboard import Scoreboard

MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x  =0, y = -280)        

    
    def move_turtle(self):
        self.forward(MOVE_DISTANCE)
        self.scoreboard = Scoreboard().clear()
        self.scoreboard = Scoreboard().add_score()


