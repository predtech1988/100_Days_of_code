import os

import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"


# resp = requests.get(url)
# with open("response.txt", "a+", encoding="utf-8") as f:
#     f.write(resp.text)
with open("Day_45\\response.txt", encoding="utf-8") as f:
    page = f.read()

soup = BeautifulSoup(page, "lxml")
# lst = soup.find_all(class_="jsx-4245974604")
data = soup.find_all(class_="jsx-3821216435 listicle-item")
with open("Day_45\\data.txt", "w", encoding="utf-8") as f:
    f.write(data[1].get_text())
