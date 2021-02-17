# https://repo.telematika.org/project/appbrewery_100-days-of-python/
#import colorgram
#colorss = colorgram.extract("Day_18\hirst_painting\image.jpg", 10)
# colors = []
# for col in range(len(colorss)):
#     tmp_color = colorss[col]
#     rgb = tmp_color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     ret_color = (r, g, b)
#     colors.append(ret_color)
from turtle import Turtle, Screen
from random import randint

colors = [(246, 210, 190), (225, 242, 249), (229, 149, 97), (136, 148, 188), (89, 96, 125),
          (232, 214, 220), (214, 79, 60), (186, 147, 160), (113, 117, 159), (189, 67, 52)]

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.penup()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.setpos(-280, -280)

x_pos = -280
y_pos = -280
for x in range(10):  
    for i in range(10):    
        timmy_the_turtle.dot(20, colors[randint(0,9)])
        timmy_the_turtle.forward(50)
    y_pos += 50
    timmy_the_turtle.setpos(x_pos, y_pos)    

#timmy_the_turtle.down()











screen.exitonclick()