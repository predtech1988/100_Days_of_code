#Compare A: Real Madrid CF, a Football club, from Spain.
#Compare B: Real Madrid CF, a Football club, from Spain.
#Add chek if folowers ==, remove TESTING
from game_data import data 
from secrets import choice, randbelow

def get_random_person():
    pointer = randbelow(len(data))
    return data.pop(pointer)

def string_format(dict, letter):
    name = dict["name"]
    description = dict["description"]
    country = dict["country"]
    tmp = dict["follower_count"]
    return f"Compare {letter}: {name}, a {description}, from {country}. TESTSING {tmp}"

def game():
    is_continue = True
    score = 0
    thing_a = get_random_person()
    thing_b = get_random_person()

    while is_continue:
        print(string_format(thing_a, "A"))
        print("VS.")
        print(string_format(thing_b, "B"))
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == "a":
            if thing_a["follower_count"] > thing_b["follower_count"]:
                score +=1
                print(f"You're right! Current score: {score}.")
                thing_a = thing_b
                thing_b = get_random_person()
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                is_continue = False
        elif user_choice == "b":
            if thing_b["follower_count"] > thing_a["follower_count"]:
                score +=1
                print(f"You're right! Current score: {score}.")
                thing_a = thing_b
                thing_b = get_random_person()
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                is_continue = False
        else:
            print("Wrong choce. Exiting!")
game()
