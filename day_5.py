def turn_around():
    turn_left()
    turn_left()
  
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




        
