#Add
import os

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return None
    return n1 / n2

commands = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    os.system("cls")
    num1 = float(input("Enter 1st number: "))

    for command in commands:
        print(command)
    operation = input("Chose operayion from thle lines above: ")
    if operation in commands:
        num2 = float(input("Enter 2st number: "))
        function = commands[operation]
        answer = function(num1, num2)
        if not answer == None:
            print(f"{num1} {operation} {num2} = {answer}")
            is_run = True
        else:
            print("Can't divede by 0! Exiting program!")
            exit()
    else:
        print(f"Sorry yhere is no {operation} command! Exiting!")
    while is_run:
        print(f"Type 'y' to continue calculating with {answer},  type 'n' to new calculation , or type 'e' to exit : ")
        decigion = input().lower()
        if decigion == "y":
            operation = input("Chose operayion from thle lines above: ")
            if operation in commands:
                num3 = float(input("Enter 2st number: "))
                function = commands[operation]
                new_answer = function(answer, num3)
                if not new_answer == None:
                    print(f"{answer} {operation} {num3} = {new_answer}")
                    is_run = True
                else:
                    print("Can't divede by 0! Exiting program!")
                    exit()                 
            else:
                print(f"Sorry yhere is no {operation} command! Exiting!")
                exit()
        elif decigion == "n":
            calculator()
        else:
            is_run = False
            print("Bye bye")
            exit()
    

calculator()

