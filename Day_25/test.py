import turtle
import pandas

states = pandas.read_csv("Day_25/50_states.csv")
#right_answers = [] #Contains right answers un str format
map_labels = []
states_to_learn = []


right_answers = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 
'Kansas', 'Louisiana', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def what_to_learn():
    all_staes_list = states.state.to_list()
    print(all_staes_list)
    for state in all_staes_list:
        if not (state in right_answers):
            states_to_learn.append(state)

    new__data = pandas.DataFrame(states_to_learn)
    with open("Day_25/states_to_learn.csv", "w") as f:
        f.write(new__data.to_csv())

    #Удалить дубли из all_staes прогнав через него списко ихвестных
what_to_learn()
#print(states_to_learn)