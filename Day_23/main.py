import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

cars_quantity = 453
game_speed = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.colormode(255)

scoreboard = Scoreboard()

player = Player()

screen.onkey(fun= player.move_turtle, key= "Up")

#Generating cars array
cars_list = []

def car_generator(cars_quantity):
    for i in range(cars_quantity):
        random_car = Cars()        
        cars_list.append(random_car)

car_generator(cars_quantity)

game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    screen.update()

    for car in cars_list:
        #print(player.distance(car))
        if player.distance(car) < 30:
            screen.clear()
            #call game_over
            scoreboard.game_over()
            game_is_on = False
        else:
            car.move_car()

    if player.ycor() > 280:
        #Encreace car's speed
        scoreboard.add_score()
        player.goto(x  =0, y = -280)
        game_speed -= 0.02


