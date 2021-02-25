weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {weekday: (c_temp * 9/5) + 32 for (weekday, c_temp) in weather_c.items()}

print(weather_f)











# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# words_list = sentence.split(" ")
# result = {word: len(word) for word in words_list}

# print(result)
# #print(result)


# def  read_file(file_name):
#     """Read a file and save to list as number. Try intersection()"""
#     result = []
#     with open(f"Day_26/{file_name}") as f:
#         result = [int(line.split("\n")[0]) for line in f]
#         #print(len(f.readlines()))
#         return result

# def  read_file(file_names):
#     """Read a file and save to list as number
#         v2 read 2 files and combine in one list,
#         return list with coresponding numbers
#     """
#     result = []
#     total = []
#     for file_name in file_names:
#         with open(f"Day_26/{file_name}") as f:
#             result.append( [int(line.split("\n")[0]) for line in f])
#     for row in result:
#         for number in row:
#             total.append(number)
#     return total

# def chaeck_coresponding(lis_to_check): #Bad idea
#     result = []
#     for number in lis_to_check:
#         if lis_to_check.count(number) >= 2:
#             result.append(number)
#     return result



# Write your code above 👆

#print(result)
#f"Day_26/{file_name}.csv"

# def chaeck_coresponding(list_1, list_2): 
#     result = []
#     for num in list_1:
#         if num in list_2 and not num in result :
#             result.append(num)
#     return result

# def chaeck_coresponding(list_1, list_2): 
#     result = []
#     result = [num for num in list_1 if num in list_2 and not num in result ]
#     return result


# num_1 = read_file("file1.txt")
# num_2 = read_file("file2.txt")
# result = chaeck_coresponding(num_1, num_2)
# print(result)


