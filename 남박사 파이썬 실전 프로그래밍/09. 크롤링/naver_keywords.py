import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.naver.com")
bs = BeautifulSoup(r.text, "lxml")

# lists = bs.find_all("li", {"class": "ah_item"})

# for li in lists:
#     title = li.find("span", {"class": "ah_k"}).text
#     print(title)

lists = bs.select("li.ah_item")
for li in lists:
    title = li.select("span.ah_k")[0].text
    print(title)