import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day_25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv("Day_25/50_states.csv")
right_answers = []
map_labels = []
states_to_learn = []

def new_map_label(state_name):
    row = states[states.state == state_name]
    label = turtle.Turtle()
    label.ht()
    label.penup()
    label.goto(x = int(row.x), y = int(row.y))
    label.write(f" {state_name}", False, "center", ("Curier", 8, "normal"))
    map_labels.append(label)

def what_to_learn():
    all_staes_list = states.state.to_list()
    print(all_staes_list)
    for state in all_staes_list:
        if not (state in right_answers):
            states_to_learn.append(state)

    new__data = pandas.DataFrame(states_to_learn)
    with open("Day_25/states_to_learn.csv", "w") as f:
        f.write(new__data.to_csv())



while len(right_answers) < 50:
    user_input = screen.textinput(f"{len(map_labels)}/50 States Correct", "What's another state name?").title()

    if user_input == "Exit":

        break

    if user_input in states.values and user_input not in right_answers:
        print("new item")
        new_map_label(user_input)
        right_answers.append(user_input)

        #pass to function and create map label
    else:
        print("Already exists, or no such state")
        #ask new state







screen.exitonclick()


