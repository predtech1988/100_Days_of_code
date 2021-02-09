import secrets
correct = secrets.randbelow(101)
if correct == 0:
    correct = secrets.randbelow(101)
lives = 10
is_continue = True
def guess_number(user_guess_number):
    if user_guess_number == correct:        
        global is_continue
        is_continue = False
        return("You are WIN!!!")
    elif user_guess_number < correct:
        return(f"Too LOW. You have {lives -1} attemps left")
    else:
        return(f"Too HIGH. You have {lives -1} attemps left")


print(f"\t Welcome to Guess number Game! \n I'am thinking of a number between 1 and 100")
difficulty = input("Chose difficulty. Type 'easy' or  'hard': ").lower()
if not (difficulty == "hard") and not (difficulty == "easy"):
    print("You entered wrong difficulty! Exiting!")
    exit()
elif difficulty == "hard":
    lives = 5
while is_continue:
    if lives == 0:
        is_continue = False
        print("You are lose!")    
    elif is_continue == False:
        print("You are lose!")
    user_guess = int(input("Make a guess: ")) 
    print(guess_number(user_guess))
    lives -= 1


    