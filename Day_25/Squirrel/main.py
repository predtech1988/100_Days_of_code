#"Day_20\snake_game\data.txt"
import csv
import pandas

# with open("Day_25\weather_data.csv") as f:
#     some_list.append(f.readlines())

# print (some_list)

# with open("Day_25\weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
# print (temperatures)

# data = pandas.read_csv("Day_25\weather_data.csv")

# mondey = data[data.day == "Monday"]
# calcium = int( mondey.temp) * (9/5) + 32
# print(calcium)

data = pandas.read_csv("Day_25\/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors_list = data["Primary Fur Color"].to_list()
searching_colors = ["Gray","Cinnamon", "Black"]

#print(data["Primary Fur Color"]) #Colors
grey_ =  colors_list.count("Gray")
print(grey_)

# def count_colors(data_list, search_colors):
#     result = dict()
#     for color in searching_colors:
#         quantity = colors_list.count(color)
#         result[color] = quantity
#     return result

def count_colors(data_list, search_colors):
    result = dict()
    col = []
    count = []
    for color in searching_colors:
        quantity = colors_list.count(color)
        col.append(color.lower())
        count.append(quantity)
    result["Fur color"] = col
    result["Count"] = count
    return result


# rr = count_colors(colors_list, searching_colors)
# answer = pandas.DataFrame(rr)
# print(answer.to_csv())

print(pandas.DataFrame(count_colors(colors_list, searching_colors)).to_csv())
