import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

player = Player()
#cars = Cars()


screen.onkey(fun= player.move_turtle, key= "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        #Encreace car's speed
        scoreboard.add_score()
        player.goto(x  =0, y = -280) 

