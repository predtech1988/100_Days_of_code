############### Blackjack Project #####################
#https://repl.it/@predtech/blackjack-final
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import os
import secrets
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


is_start = input("Welcome to BlackJack, start game? 'y' or 'n' ")

if is_start == "n":
    exit()
users_cards = []
ai_cards = []

def generte_cards(who, times):
    for i in range(times):
        card = secrets.randbelow(13)
        if who == "user":
            users_cards.append(cards[card])
        else:
            ai_cards.append(cards[card])

def get_score(who):
    score = 0
    if who == "user":
        for card in users_cards:
            score += card
    else:
        for card in ai_cards:
            score += card
    return score




def main_module():
    os.system("cls")
    print("Lets start")
    generte_cards("user", 2)
    generte_cards("ai", 2)
    user_score = get_score("user")
    ai_score = get_score("ai")
    if user_score == 21:
        print(f"\t Your cards:{users_cards}, current score: {user_score} ")
        print(f"Computer's first card is: {ai_cards[0]}")
        print("You are winner!!!")
        exit()
    elif ai_score == 21:
        print(f"\t Your cards:{users_cards}, current score: {user_score} ")
        print(f"Computer's first card is: {ai_cards[0]}")
        print("YOu lose! Computer have Black Jack!!!!")
        exit()
    else:
        print(f"\t Your cards:{users_cards}, current score: {user_score} ")
        print(f"Computer's first card is: {ai_cards[0]}")
        new_card = input("Type 'y' to get another card, type 'n' to pass:")
        if new_card == "yes":
            print("Sorry not emplemented. Exiting app!")
            exit()
        else:
            #count score and chose winner
            #Your final hand: [4, 8], final score: 12
            #Computer's final hand: [10, 10], final score: 20
            #You lose 😤
            #Do you want to play a game of Blackjack? Type 'y' or 'n': GO TO START  Draw ?
            print("Sorry not emplemented. Exiting app!")
            exit()

main_module()
