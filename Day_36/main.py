import os
from random import randint
from typing import Any, Dict, List

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# STOCK = "IKT"
# COMPANY_NAME = "Inhibikase Therapeutics, Inc"

twilio_api_keys = os.getenv("weather_api")
account_sid = twilio_api_keys.split(",")[1]
auth_token = twilio_api_keys.split(",")[2]
message_to = twilio_api_keys.split(",")[3]
client = Client(account_sid, auth_token)

alphavantage_endpoint = "https://www.alphavantage.co/query"
alphavantage = ""  # API_KEY for stock data
parameteres: Dict[str, Any] = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": alphavantage,
}

# Getting stock information
response = requests.get(url=alphavantage_endpoint, params=parameteres)
raw_data = response.json()


def get_stock_data(data):
    data_list = []
    flag = 0  # Flag = day's, we need only two for yesterday and day before yesterday
    for key, value in data["Time Series (Daily)"].items():
        if flag == 2:
            break
        data_list.append(value)
        flag += 1
    yesterday_price = float(data_list[0]["4. close"])
    day_before_yesterday = float(data_list[1]["4. close"])
    difference = abs(day_before_yesterday - yesterday_price)
    return (yesterday_price, day_before_yesterday, difference)


def get_percentage_diff(data):
    difference = data[2]
    yesterday_price = data[0]
    diff_percent = (difference / yesterday_price) * 100
    if diff_percent >= 5.0:
        get_stock_news(COMPANY_NAME)
    else:
        print(f"Difference lower than 5%, and = {diff_percent}")


def send_sms(text):
    """
    Sending sms with random article title
    """
    random_article: int = randint(0, 2)
    sms_body: str = text[random_article]["title"]
    message = client.messages.create(
        body=sms_body,
        from_="+14155786329",
        to=message_to,
    )
    print(message.status)
    print(sms_body)


def get_stock_news(stock):
    news_api = ""  # Add your key
    url_end_point = "https://newsapi.org/v2/everything"
    parameteres = {
        "apiKey": news_api,
        "q": stock,
        "sortBy": "publishedAt",
        "pageSize": 10,
    }
    news_response = requests.get(url=url_end_point, params=parameteres).json()
    if news_response["status"] != "ok":
        print("Error!" + news_response["message"])
        return
    news_list: List[Dict[str, str]] = []
    for i in range(3):  # Getting 3 first articles
        news: Dict[str, str] = {
            "title": news_response["articles"][i]["title"],
            "description": news_response["articles"][i]["description"],
        }
        news_list.append(news)
    send_sms(news_list)


if __name__ == "__main__":
    print(type(raw_data))
    if "Error Message" in raw_data:
        print("Error!")
        raise NameError("Can't get data from the https://www.alphavantage.co")
    current_data = get_stock_data(raw_data)
    get_percentage_diff(current_data)
