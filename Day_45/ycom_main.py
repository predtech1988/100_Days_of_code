import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/newest"

resp = requests.get(url=url)
page = resp.text

soup = BeautifulSoup(page, "html.parser")
first_article_text = soup.find(name="a", class_="storylink").get_text()
first_article_link = soup.find(name="a", class_="storylink").get("href")
article_score = soup.find(name="span", class_="score").get_text()
print(first_article_link, article_score)
