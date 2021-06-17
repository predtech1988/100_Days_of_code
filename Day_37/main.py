import datetime
import os
import time
from typing import Dict

import requests

pixela_endpoint: str = "https://pixe.la/v1/users"
account_sid: str = os.getenv("weather_api").split(",")[1]  # Taking an API token as a password
user_params: Dict[str, str] = {
    "token": account_sid,
    "username": "alexk88",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating new User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# print(response.json()["isSuccess"])
graph_endpoint = pixela_endpoint + "/" + user_params["username"] + "/graphs"
headers: Dict[str, str] = {"X-USER-TOKEN": account_sid}
graph_params: Dict[str, str] = {
    "id": "graph1",
    "name": "Coding_days",
    "unit": "days",
    "type": "int",
    "color": "shibafu",
}

# Creating new graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
# id = graph_params["id"]

# Set current date in propper format yyyyMMdd or just use .strftime("%Y%m%d") ^_^
now = time.localtime(time.time())
mon = now.tm_mon
day = now.tm_mday
if mon < 10:
    mon = "0" + str(mon)
if day < 10:
    day = "0" + str(day)
date = f"{now.tm_year}{mon}{day}"

add_pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"

pixel_params: Dict[str, str] = {
    "date": date,
    "quantity": "1",
}
# responce = requests.put(url=add_pixel_endpoint, json=pixel_params, headers=headers)
# print(responce.text)


def update_pixel(date, quantity):
    # /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
    update_endpoint = f"{graph_endpoint}/{graph_params['id']}/{date}"
    params: Dict[str, str] = {
        "quantity": str(quantity),
    }
    responce = requests.put(url=update_endpoint, json=params, headers=headers)
    print(responce.text)


date_to_update = datetime.datetime(year=2021, month=6, day=11).strftime("%Y%m%d")
update_pixel(date_to_update, 2)
