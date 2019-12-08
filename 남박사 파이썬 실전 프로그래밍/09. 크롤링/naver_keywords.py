import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.naver.com")
bs = BeautifulSoup(r.text, "html.parser")

lists = bs.find_all("li", {"class": "ah_item"})

for li in lists:
    title = li.find("span", {"class": "ah_k"}).text
    print(title)