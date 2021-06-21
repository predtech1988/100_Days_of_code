# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch

sheety = DataManager()
# sheet_data = sheety.sheety_get_data()
sheet_data = [
    {"city": "Paris", "iataCode": "PAR", "id": 2, "lowestPrice": 54},
    {"city": "Berlin", "iataCode": "BER", "id": 3, "lowestPrice": 42},
    {"city": "Tokyo", "iataCode": "TYO", "id": 4, "lowestPrice": 485},
    {"city": "Sydney", "iataCode": "SYD", "id": 5, "lowestPrice": 551},
    {"city": "Istanbul", "iataCode": "IST", "id": 6, "lowestPrice": 95},
    {"city": "Kuala Lumpur", "iataCode": "KUL", "id": 7, "lowestPrice": 414},
    {"city": "New York", "iataCode": "NYC", "id": 8, "lowestPrice": 240},
    {"city": "San Francisco", "iataCode": "SFO", "id": 9, "lowestPrice": 260},
    {"city": "Cape Town", "iataCode": "CPT", "id": 10, "lowestPrice": 378},
]


def check_iata_code(lst):
    iata = FlightSearch()
    for item in lst:
        if item["iataCode"] == "":
            iata.add_iata_code(item)


# pprint(data)
check_iata_code(sheet_data)
