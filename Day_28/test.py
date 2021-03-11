lst = []
for num in range(1,18):
    if num%2 == 0:
        lst.append(num)
    
print (lst) 


for reps in lst:
    if reps % 2 == 0 and reps%8 == 0:
        print(reps)