import datetime

import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"


def get_date_from_user():
    user_input = input("Enter  date in formart YYYY-MM-DD like:2020-01-20 ")
    tm = datetime.datetime(
        year=int(user_input.split("-")[0]),
        month=int(user_input.split("-")[1]),
        day=int(user_input.split("-")[2]),
    )
    tm = tm.strftime("%Y-%m-%d")
    return tm


def grab_site_page(date):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept-Language": "ja",
        "Referer": "https://www.google.com/",
    }
    resp = requests.get(url=URL + date, headers=headers)
    return resp


def save_song_in_file(data):
    with open("Day_46/songs_list.txt", "a+") as file:
        file.write(data)


def gether_song_artist(resp):
    soup = BeautifulSoup(resp.text, "html.parser")
    songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
    artists = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")
    print(type(songs))
    i = 0
    for song in songs:
        tmp_string = f"{artists[i].get_text()} - {song.get_text()} \n"
        i += 1
        save_song_in_file(tmp_string)


def start_app():
    chart_date = get_date_from_user()
    site_page = grab_site_page(chart_date)
    gether_song_artist(site_page)


if __name__ == "main":
    start_app()
