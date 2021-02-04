
#Write your code below this line 👇
def prime_checker(number):
    score = []
    if number == 1:
        print("NO!!!")
    else:    
        for num in range(1, number + 1):
            if (number % num) == 0:
                score.append(0)
                pass
        #print(score)
        if score.count(0) > 2:
            #pass
            print(f"{number} is NOOO!!")
        else:
            #pass
            print(f"{number} is Prime!")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
#prime_checker(3)
"""
for i in range(1,14):
    prime_checker(i)

"""