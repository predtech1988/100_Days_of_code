import random
#List of words
#Слова конечно  должны относиться к одной теме :)
#Можно добавить выбор темы к которй тносятся слова: фрукты, овощи, животные итд, 
words = ["wabi", "sensei", "love" "apple", "education", "nihongo"]
word = random.choice(words)
answer = []
for x in range(len(word)):
    answer.append("*")
lives = 6
score = 0

#print(word)
print("".join(answer))

#По позиции * меняем на букву
def char_position(word, symbol): 
    for char in range(len(word)):
        if word[char] == symbol:
            answer[char] = symbol

while lives > 0 and score < len(word): #Если жизней больше 0 и отагадны не все буквы, повторяем запрос ввода
    user_input = input("\n" + "Enter the letter: ").lower()
    if user_input in word and not(user_input in answer): #Если введённый символ есть в слове и уже не был отгадан до этого
        score += word.count(user_input) #Ведём учёт отгаданных букв
        char_position(word, user_input) #Заменяем *
        print("Good!")
        print("Word: " + "".join(answer))
        print(f"Lives left: {lives}")
        if  score == len(word):
            print("おめでとうございます")
    else:
        lives -= 1 #Если не угадали букву минус одна жизнь
        print("Nope")
        print("Word: " + "".join(answer))
        print(f"Lives left: {lives}")
else:
    if score > len(word) or lives == 0:
        print("Try again :( ")
    