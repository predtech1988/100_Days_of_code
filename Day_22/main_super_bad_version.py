#Pong game
from turtle import Turtle, Screen
import time
from pad import Pad
from scoreboard import Scoreboard
from ball import Ball
from walls import Wall

game_is_running = True

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.listen()

ball = Ball()

pad_r = Pad((350, 0))
pad_l = Pad((-350, 0))

scoreboard_ = Scoreboard(pad_r, pad_l)

screen.onkey(pad_r.move_up, "Up")
screen.onkey(pad_r.move_down, "Down")

screen.onkey(pad_l.move_up, "w")
screen.onkey(pad_l.move_down, "s")
screen.onkey(ball.ball_curren_position, "space") 

upper_wall = Wall((0, 290))
direction = "up_r"


def is_collide():
    if ball.distance(upper_wall) == 295:
        direction = "down"
        return True

        


while game_is_running:
    screen.update()
    time.sleep(0.1) 
    #print(ball.ycor())
    #print(int(ball.distance(pad_r)))
    ball.ball_move(direction)
    if ball.ycor() >= 285 and ball.xcor() > 0:
        direction = "down_r"
        print(direction)

    elif ball.ycor() >= 285 and ball.xcor() < 0:
        direction = "down_l"
        print(direction)

    elif ball.ycor() <= -285 and ball.xcor() > 0:
        direction = "up_r"
        print(direction)

    elif ball.ycor() <= -285 and ball.xcor() < 0:
        direction = "up_l"
        print(direction)

    if int(ball.distance(pad_r)) < 40:
        print("Hit R_PAD")
        pad_r.current_score +=1
        scoreboard_.update_scores(pad_l, pad_r)
        direction = "left"
        print(direction)
        
    elif int(ball.distance(pad_l)) < 40:
        print("Hit L_PAD")
        pad_l.current_score +=1
        scoreboard_.update_scores(pad_l, pad_r)
        direction = "right"
        print(direction)

    if ball.xcor() > 345 or ball.xcor() < -345:
        print("YOU LOSE!")
        scoreboard_.game_over()
        game_is_running = False



    # if ball.ycor() >= 285 or ball.ycor() <= -285:
    #     print("WALL HIT")
    #     ball.ball_change_direction()





screen.exitonclick()