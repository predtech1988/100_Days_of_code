#Compare A: Real Madrid CF, a Football club, from Spain.
#Compare B: Real Madrid CF, a Football club, from Spain.
#Add chek if folowers ==
from game_data import data 
from secrets import choice, randbelow


is_continue = True


def get_random_person():
    pointer = randbelow(len(data))
    #print(data.pop(pointer))
    return data.pop(pointer)

def check_user_choise(user_choise, a, b, user_score):
    """
    Takes user choise, A and B person profiles, User score.
    Returns list [score, string with mesage, continue (True/False), new A or B]
    

    """
    compare_a = a
    compare_b = b
    score = user_score
    answer_returned = []
    if user_choise == "a":
        if compare_a["follower_count"] >= compare_b["follower_count"]:
            score += 1
            return [score, f"You're right! Current score: {score}.", True, compare_b]
        else:
            return [score,f"Sorry, that's wrong. Final score: {score}", False, compare_a]
    elif user_choise == "b":
        if compare_b["follower_count"] >= compare_a["follower_count"]:
            score += 1
            return [score, f"You're right! Current score: {score}.", True, compare_b]
        else:
           return [score,f"Sorry, that's wrong. Final score: {score}", False, compare_b]
    else:
        print("Line 49 something wrong!")   

def game():
    pass

compare_a = get_random_person()
user_score = 0
while is_continue:
    compare_b = get_random_person()    
    name_a = compare_a["name"]
    description_a = compare_a["description"]
    country_a = compare_a["country"]

    name_b = compare_b["name"]
    description_b = compare_b["description"]
    country_b = compare_b["country"]

    tmp1 = compare_a["follower_count"]
    tmp2 = compare_b["follower_count"]

    print(f"Compare A: {name_a}, a {description_a}, from {country_a}. TESTSING {tmp1}")
    print("VS.")
    print(f"Against B: {name_b}, a {description_b}, from {country_b}. TESTSING {tmp2}")
    user_choise = input("Who has more followers? Type 'A' or 'B': ").lower()
    answer = check_user_choise(user_choise, compare_a, compare_b, user_score)
    print(answer[1])
    is_continue = answer[2]
    compare_a = answer[3]
    user_score = answer[0]
    