import json
import os
from typing import Any, Dict

import requests
from twilio.rest import Client

URL_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
weather_api = os.getenv("weather_api")  # Reading all vars from the environment vars
parameteres: Dict[str, Any] = {
    "lat": 45.383715,
    "lon": 33.121555,
    "appid": weather_api.split(",")[0],
    "exclude": "current,minutely,daily,alerts",
}
account_sid = weather_api.split(",")[1]
auth_token = weather_api.split(",")[2]
message_to = weather_api.split(",")[3]
client = Client(account_sid, auth_token)

response = requests.get(URL_ENDPOINT, params=parameteres)
print(response.status_code)
response.raise_for_status()
resp_json = json.loads(response.text)

for hour in range(12):
    weather_id = resp_json["hourly"][hour]["weather"][0]["id"]
    if weather_id < 700:
        message = client.messages.create(
            body="Today will be rainy!.",
            from_="+14155786329",
            to=message_to,
        )
        print(weather_id)
        print(message.status)
        break
