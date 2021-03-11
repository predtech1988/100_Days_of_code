import requests
import datetime as dt
import time

MY_LONG = 33.114799
MY_LAT = 45.377901
UTC_SHIFT = 3

time_now = dt.datetime.now()
# print(time_now)


def get_sunsen_sunrise():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")
                  [1].split(":")[0]) + UTC_SHIFT
    sunset = int(data["results"]["sunset"].split("T")
                 [1].split(":")[0]) + UTC_SHIFT
    return sunrise, sunset


def get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_long = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])    
    return iss_long, iss_lat


def check_is_iss_visible():
    iss_long, iss_lat = get_iss_location()
    sunrise, sunset = get_sunsen_sunrise()
    if time_now.hour >= sunset and time_now.hour <= sunrise:
        print("Ok it is night, you can check coordinates of ISS")
        lat_diff = MY_LAT - iss_lat
        long_diff = MY_LONG - iss_long
        if( lat_diff >= -5 and lat_diff <= 5) and (long_diff >= -5 and long_diff <= 5):
            print("You can see ISS")
            #call send email function
    else:
        print("It's day time, you can't see ISS :(")
        #измерить разницу во времени сколько осталось подождат ьи вернуть её, на основе сделать новый слип


# print(sunrise)
#check_is_iss_visible()
#print(get_iss_location())
#check_is_iss_visible()
while True:
    check_is_iss_visible()
    time.sleep(10)

