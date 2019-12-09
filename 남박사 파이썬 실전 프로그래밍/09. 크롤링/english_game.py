import requests
from bs4 import BeautifulSoup

url = "https://www.usatoday.com/"
r = requests.get(url)
bs = BeautifulSoup(r.text, "lxml")
lists = bs.select("div.gnt_m_th > a")
for li in lists:
    href = li["href"]
    print(href)