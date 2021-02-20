# some tetriss
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

game_is_running = True

snake_ = Snake(number=3)
food = Food()
scoreboard_ = Scoreboard()

screen.listen()
screen.onkey(snake_.up, "Up")
screen.onkey(snake_.down, "Down")
screen.onkey(snake_.left, "Left")
screen.onkey(snake_.right, "Right")

while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake_.move()

    if snake_.turtles_list[0].distance(food) < 15:
        print("Eat it")
        food.update_food_position()
        scoreboard_.add_score()
        snake_.new_segmaent(1)

    if snake_.turtles_list[0].xcor() > 280 or snake_.turtles_list[0].xcor() < -280 or snake_.turtles_list[0].ycor() > 280 or snake_.turtles_list[0].ycor() < -280:
        print("YOU LOSE!")
        scoreboard_.game_over()
        game_is_running = False

    for snake_segment in snake_.turtles_list[1:]:
        if snake_.turtles_list[0].distance(snake_segment) < 10:
            print("YOU LOSE!")
            scoreboard_.game_over()
            game_is_running = False


screen.exitonclick()
