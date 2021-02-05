#https://repl.it/@appbrewery/blind-auction-start
import os
os.system("cls")
print("Welcome to secret auction")
continue_auction = True
members = dict()
maxx = 0
name = ""

while continue_auction == True :
    member_name = input("What is your name?: ")
    member_bid = int(input("What is your bid?:$ "))
    members[member_name] = member_bid
    is_continue = input("Is there anonther bidder's? Type: 'yes', 'no' ").lower()
    if is_continue == "yes":
        os.system("cls")
        continue
    else:
        os.system("cls")
        continue_auction = False

for key, value in members.items():
    if  maxx < value:
        maxx = value
        name = key

print(f"The winner is {name} , with ${maxx} bid!")


