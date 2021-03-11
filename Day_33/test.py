import requests
import datetime as dt

MY_LAT = 45.377901
MY_LONG = 33.114799
UTC_SHIFT = 3

iss_lat = 161.0306
iss_long = 48.0816


time_now = dt.datetime.now()

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# iss_lat = data["iss_position"]["latitude"]
# iss_long = data["iss_position"]["longitude"]

# print(iss_lat, iss_long)

def coord_diff():
    lat_diff = MY_LAT - iss_lat
    long_diff = MY_LONG - iss_long
    if( lat_diff >= -5 and lat_diff <= 5) and (long_diff >= -5 and long_diff <= 5):
        print("You can see ISS")
        #call send email function
    #return long_diff, lat_diff
print(coord_diff())