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






while game_is_running:
    screen.update()
    time.sleep(0.1) 
    print(ball.xcor())
    #print(int(ball.distance(pad_r)))

    ball.ball_move()
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.ball_bounce_y()


    if int(ball.distance(pad_r)) < 50 and ball.xcor() > 330:
        print("Hit R_PAD")
        pad_r.current_score +=1
        scoreboard_.update_scores(pad_l, pad_r)
        ball.ball_bounce_x()

        
    elif int(ball.distance(pad_l)) < 50 and ball.xcor() < -330:
        print("Hit L_PAD")
        pad_l.current_score +=1
        scoreboard_.update_scores(pad_l, pad_r)
        ball.ball_bounce_x()


    if ball.xcor() > 355 or ball.xcor() < -355:
        print("YOU LOSE!")
        scoreboard_.game_over()
        game_is_running = False



    # if ball.ycor() >= 285 or ball.ycor() <= -285:
    #     print("WALL HIT")
    #     ball.ball_change_direction()





screen.exitonclick()