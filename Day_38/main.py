import datetime
import os
import time
from typing import Dict

import requests


def sheety_send_workout(exercise, duration, calories):
    tm = datetime.datetime.now()
    endpoint = "https://api.sheety.co/40bfbacef3b2aa0e9faed02c5fb76ea5/workouts/workouts"
    headers = {
        "Authorization": "Bearer xxx_secret_xxx",
        "Content-Type": "application/json",
    }
    workout = {
        "workout": {
            "date": tm.strftime("%d/%m/%Y"),
            "time": tm.strftime("%X"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }
    resp = requests.post(url=endpoint, headers=headers, json=workout)
    print(resp.text)


def get_workut_data(query):
    BASE_URL = "https://trackapi.nutritionix.com/v2/"

    headers: Dict[str, str] = {
        "x-app-id": os.getenv("nutritionix").split(",")[0],
        "x-app-key": os.getenv("nutritionix").split(",")[1],
        "x-remote-user-id": "0",
    }

    nutrients_endpoint = BASE_URL + "natural/nutrients"  # Food
    params_food = {
        "query": "for breakfast i ate 2 eggs, bacon, and french toast",
        "timezone": "Moscow Time",
    }
    # resp = requests.post(url=nutrients_endpoint, headers=headers, json=params_food)

    exercise_endpoint = BASE_URL + "natural/exercise"
    params_exercise = {
        "query": query,
        "gender": "male",
        "weight_kg": 90,
        "height_cm": 186,
        "age": 52,
    }
    resp = requests.post(url=exercise_endpoint, headers=headers, json=params_exercise).json()["exercises"][0]
    sheety_send_workout(
        exercise=resp["name"].title(),
        duration=resp["duration_min"],
        calories=resp["nf_calories"],
    )


def sheety_get_workouts(id=None):  # Also we can use *args if len(args) == 0 ....
    if id != None:
        endpoint = f"https://api.sheety.co/40bfbacef3b2aa0e9faed02c5fb76ea5/workouts/workouts/{id}"
    else:
        endpoint = "https://api.sheety.co/40bfbacef3b2aa0e9faed02c5fb76ea5/workouts/workouts"
    headers = {
        "Authorization": "Bearer xxx_secret_xxx",
    }
    resp = requests.get(url=endpoint, headers=headers)
    print(resp.text)


user_input = input("Witch exercise do you did? ")
get_workut_data(user_input)
