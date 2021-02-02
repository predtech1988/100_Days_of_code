#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_rigth():
    turn_left()
    turn_left()
    turn_left()
        
def jump_1():
        turn_left()
        move()
        turn_rigth()
        
while not(at_goal()):
    turn_left()
    if wall_on_right():
        turn_rigth()
        jump_1()
        if front_is_clear():
            move()
            turn_rigth()
            if front_is_clear():
                while front_is_clear():
                    move()
                turn_left()            
    else:
        turn_rigth()
        move()