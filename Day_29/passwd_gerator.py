#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_random_password():
    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 3)

    #password_list = []

    password_list1 = [random.choice(letters) for char in range(nr_letters)]
    password_list2 = [random.choice(symbols) for char in range(nr_symbols)]
    password_list3 = [random.choice(numbers)for char in range(nr_numbers)]
    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    # random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char


    #print(f"Your password is: {password}")
get_random_password()