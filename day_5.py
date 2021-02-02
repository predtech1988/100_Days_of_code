def turn_around():
    turn_left()
    turn_left()
  
def turn_rigth():
    turn_left()
    turn_left()
    turn_left()
    
def turn_3():
    turn_left()
    turn_left()
    turn_left()
    turn_left()
    
def jump_1():
        turn_left()
        move()
        turn_rigth()

        
while not(at_goal()):    
    if front_is_clear():
        move()
    elif wall_in_front():
        jump_1()

    elif wall_on_right():
        jump_1()
