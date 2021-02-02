#Password Generator Project 

"""
Ссылка на задание:
https://repl.it/@appbrewery/password-generator-start
Нужно создать несколкьо реализаций генератора паролей
Всего здесь 3 реализации, я их никак не разделял, поэтому они будут 
одновременно выдавать результат.
"""
#
#
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Достаточн опростое задание, но можно было и красивее сделать:)

password = ""
for i in range(nr_letters):
  password += letters[random.randint(0, len(letters) -1)]

for i in range(nr_numbers):
  password += numbers[random.randint(0, len(numbers) -1)]

for i in range(nr_symbols):
  password += symbols[random.randint(0, len(symbols) -1)]

print(f"Easy level password is: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
"""
Очень кривая реализация прям костыльные костыли, если пароль длинный
то рандомизация выходит слабая.
После просмотра видео с ответом, понял что можно было бы взять 
предыдущий код, и вмест остроки password сделать список, а 
в конце к нему просто применить random.shuffle() :))
"""

passwd_1 = ""
passwd_2 = ""

for i in range(nr_letters):
  rnd_cell = random.randint(0, 1)
  if rnd_cell == 0:  
    passwd_1 += letters[random.randint(0, len(letters) -1)]
  else:
    passwd_2 += letters[random.randint(0, len(letters) -1)]

for i in range(nr_numbers):
  rnd_cell = random.randint(0, 1)
  if rnd_cell == 0: 
    passwd_1 += numbers[random.randint(0, len(numbers) -1)]
  else:
    passwd_2 += numbers[random.randint(0, len(numbers) -1)]

for i in range(nr_symbols):
  rnd_cell = random.randint(0, 1)
  if rnd_cell == 0: 
    passwd_1 += symbols[random.randint(0, len(symbols) -1)]
  else:
    passwd_2 += symbols[random.randint(0, len(symbols) -1)]
hard_level_password = passwd_1 + passwd_2
print(f"Hard level password is: {hard_level_password}")

#Hard Level V2 - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
"""
Это я уже после просмотра ответа сделал, не знал о random.choice() 
и random.shuffle() а после того как глянул его реализацию в родной 
библиотеке прицныл очень просто реализванно, мог-бы и сам догадаться, 
как такое сделать и без этого метода. 
"""

passwd_array= []

for char in range(1, nr_letters + 1):
  passwd_array.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
  passwd_array.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
  passwd_array.append(random.choice(symbols))

random.shuffle(passwd_array)
final_password = "".join(passwd_array)
print(f"Hard Level password V2: {final_password}")