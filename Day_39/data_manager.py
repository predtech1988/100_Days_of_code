from typing import Any, Dict

import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def sheety_get_data(self, id: int = None) -> Dict[str, Any]:  # Also we can use *args if len(args) == 0 ....
        if id != None:
            endpoint = f"https://api.sheety.co/40bfbacef3b2aa0e9faed02c5fb76ea5/flightDeals/prices/{id}"
        else:
            endpoint = "https://api.sheety.co/40bfbacef3b2aa0e9faed02c5fb76ea5/flightDeals/prices"
        headers = {
            "Authorization": "Bearer xxx",
        }
        resp = requests.get(url=endpoint, headers=headers)
        return resp.json()["prices"]

    def sheety_update_data(self, id: int, **kwargs):
        endpoint = f"https://api.sheety.co/40bfbacef3b2aa0e9faed02c5fb76ea5/flightDeals/prices/{id}"
        headers = {
            "Authorization": "Bearer xxx",
            "Content-Type": "application/json",
        }
        price: Dict[str, Any] = {"price": {}}
        price["price"] = kwargs
        resp = requests.put(url=endpoint, headers=headers, json=price)
        print(resp.text)


# d = DataManager()
# d.sheety_get_data(8)
