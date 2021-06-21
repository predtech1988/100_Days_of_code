import datetime

import requests

from data_manager import DataManager

sheety = DataManager()
FROM = "LON"
CURRENCY = "GBP"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def add_iata_code(self, item):
        iataCode = self.get_iata_code(item["city"])
        sheety.sheety_update_data(
            id=item["id"],
            city=item["city"],
            iataCode=iataCode,
            lowestPrice=item["lowestPrice"],
        )

    def get_iata_code(self, city_name: str) -> str:
        endpoint = "https://tequila-api.kiwi.com/locations/query"
        headers = {
            "accept": "application/json",
            "apikey": "",
        }
        params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": "1",
            "active_only": "True",
        }

        resp = requests.get(url=endpoint, headers=headers, params=params).json()
        return resp["locations"][0]["code"]

    def find_flight(self, iata_code):
        date_from = datetime.datetime.now() + datetime.timedelta(days=1)
        date_to = (date_from + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
        date_from = date_from.strftime("%d/%m/%Y")

        endpoint = "https://tequila-api.kiwi.com/v2/search"
        headers = {
            "accept": "application/json",
            "apikey": "",
        }
        params = {
            "max_stopovers": 0,
            "flight_type": "round",
            "fly_from": FROM,
            "fly_to": iata_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
        }

        resp = requests.get(url=endpoint, headers=headers, params=params).json()
        print(resp)
        print("___________________________________")
        result = resp["data"][0]["price"]
        print(result)


tmp = FlightSearch()
tmp.find_flight("PAR")
