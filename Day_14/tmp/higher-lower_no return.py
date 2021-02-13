#Compare A: Real Madrid CF, a Football club, from Spain.
#Compare B: Real Madrid CF, a Football club, from Spain.
#Add chek if folowers ==
from game_data import data 
from secrets import choice, randbelow


#is_continue = True
is_continue = 0

def get_random_person():
    pointer = randbelow(len(data))
    #print(data.pop(pointer))
    return data.pop(pointer)

def check_user_choise(user_choise, a, b, user_score):
    compare_a = a
    compare_b = b
    score = user_score
    answer_returned = []
    if user_choise == "a":
        if compare_a["follower_count"] >= compare_b["follower_count"]:
            user_score += 1
            print(f"You're right! Current score: {user_score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
    elif user_choise == "b":
        if compare_b["follower_count"] >= compare_a["follower_count"]:
            user_score += 1
            print(f"You're right! Current score: {user_score}.") 
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
    else:
        print("Line 49 something wrong!")   

def game():
    pass

compare_a = get_random_person()
compare_b = get_random_person()
while is_continue < 3:
    user_score = 0
    name_a = compare_a["name"]
    description_a = compare_a["description"]
    country_a = compare_a["country"]

    name_b = compare_b["name"]
    description_b = compare_b["description"]
    country_b = compare_b["country"]

    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    print("VS.")
    print(f"Against B: {name_b}, a {description_b}, from {country_b}.")
    user_choise = input("Who has more followers? Type 'A' or 'B': ").lower()
    check_user_choise(user_choise, compare_a, compare_b, user_score)  

    is_continue +=1
    