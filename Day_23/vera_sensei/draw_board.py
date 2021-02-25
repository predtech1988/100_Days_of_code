import time
from turtle import Screen

from scoreboard import Scoreboard, FONT

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

started_scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    #print(started_scoreboard.scores)
    started_scoreboard.write(f"Level: 000000", False, "center", FONT)
    started_scoreboard.clear()