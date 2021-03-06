from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Chose winner color: ")

is_run = True
#Tim
tim = Turtle(shape="turtle")
tim.penup()
tim.color("red")
tim.goto(x = -230, y = -180)

#Bob
bob = Turtle(shape="turtle")
bob.penup()
bob.color("pink")
bob.goto(x = -230, y = -150)

#Jack
jack= Turtle(shape="turtle")
jack.penup()
jack.color("green")
jack.goto(x = -230, y = -120)

#Ron
ron= Turtle(shape="turtle")
ron.penup()
ron.color("blue")
ron.goto(x = -230, y = -90)

#Deb
deb= Turtle(shape="turtle")
deb.penup()
deb.goto(x = -230, y = -60)

print(tim.position())

turtles = [
    {"tim": tim},
    {"bob":bob},
    {"jack": jack},
    {"ron": ron},
    {"deb":deb},
]
print(type(turtles[0]))


def run(name):
    x_pos = name.position()
    print(x_pos[0])
    if x_pos[0] <= 215:
        name.forward(randint(1, 20))
        return True
    else:
        return False

while is_run:
    for turtle in turtles:
        if is_run:
            for key in turtle:
                print(key)
                result = run(turtle[key])
                if not result:
                    if user_bet == key:
                        print(f"You WINNER! {key} is first turtle!")
                        is_run = False
                        break
                    else:
                        print(f"You LOSER! {key} is first turtle!")
                        is_run = False
                        break
        else:
            break
screen.exitonclick()
