travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above.  https://repl.it/@appbrewery/day-9-2-exercise

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visitet, times_visited, cities_visited):
    new_place = {
        "country": country_visitet,
        "visits": times_visited,
        "cities": cities_visited,
    }
    travel_log.append(new_place)
        




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print(travel_log)
print(travel_log)



