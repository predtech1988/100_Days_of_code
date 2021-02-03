#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_rigth():
    turn_left()
    turn_left()
    turn_left()
def turn():
    for side in range(4):
        if not(wall_on_right()):
            turn_left()
        elif wall_in_front():
            turn_left()
        else:
            break

while not(at_goal()):
    for side in range(4):
        if not(wall_on_right()):
            turn_left()
        elif wall_in_front():
            turn_left()
        else:
            break
    if (wall_on_right()):
        move()
    else:
        turn_lef()


       


