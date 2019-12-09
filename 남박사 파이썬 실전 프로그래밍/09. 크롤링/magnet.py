import requests
from bs4 import BeautifulSoup
import re

keyword = "리눅스"
url = "https://www.google.com/search?q={0}+magnet%3A%3Fxt%3D&rlz=1C1SQJL_koKR871KR871&oq={0}+magnet%3A%3Fxt%3D".format(keyword)

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
r = requests.get(url, headers=header)
bs = BeautifulSoup(r.text, "lxml")
links = bs.select("div.g > div > div.rc > div.r > a")

for a in links:
    href = a["href"]
    text = a.select("h3")
    if len(text) <= 0:
        continue
    title = text[0].text
    print(title)
    