import pandas

data = pandas.read_csv("Day_26/nato_phonetic_alphabet.csv")

# for (index, row) in data.iterrows():
#     print(row.code)

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()

answer = [data_dict[letter] for letter in user_word ]
print(answer)



