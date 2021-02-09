import os
import secrets
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def generte_cards():
    return cards[secrets.randbelow(13)]

def get_score(arr):
    score = 0
    for card in arr:
        score += card
    if (score  == 21) and (len(arr) == 2):
        return 0
    elif (11 in arr) and score > 21:
        return score - 10
    else:
        return score

def main_module():
    #Count user and ai scores
    user_score = get_score(users_cards)
    ai_score = get_score(ai_cards)
    #print(user_score, ai_score)

    if user_score == 0:
        print("\t BlackJack! You are win!")
        print(f"AI cards:{ai_cards}")

    elif ai_score == 0:
        print("\t BlackJack! AI winner!")
        print(f"Your cards:{users_cards}")

    elif (user_score == ai_score) and (len(users_cards) > 2):
        print("\t DRAW!")
        print(f"\t Your cards:{users_cards}, current score: {user_score} ")
        print(f"AI cards:{ai_cards}, current score: {ai_score}")

    elif user_score > 21:
        print("\t YOU LOSE!")
        print(f"Your cards:{users_cards}, final score: {user_score} ")
        print(f"AI cards:{ai_cards}, final score: {ai_score}")       

    elif ai_score > 21:
        print("\t YOU WIN!")
        print(f"Your cards:{users_cards}, final score: {user_score} ")
        print(f"AI cards:{ai_cards}, final score: {ai_score}")   

    else:
        print(f"\t Your cards:{users_cards}, current score: {user_score} ")
        print(f"Computer's first card is: {ai_cards[0]} *** {ai_cards}")
        new_card = input("Type 'y' to get another card, type 'n' to pass:")
        #if "n" ai add cards while 17   
        if new_card == "y":
            users_cards.append(generte_cards())
            main_module()
        elif new_card == "n":
            if ai_score < 17:
                while ai_score < 17:
                    ai_cards.append(generte_cards())
                    ai_score = get_score(ai_cards)
            main_module()







    




is_start = input("Welcome to BlackJack, start game? 'y' or 'n' ")

if is_start == "n":
    exit()
else:
    users_cards = []
    ai_cards = []
    os.system("cls")
    print("Lets start")
    #Fill user and ai cards
    for i in range(2):        
        users_cards.append(generte_cards())
        ai_cards.append(generte_cards())
    main_module()
