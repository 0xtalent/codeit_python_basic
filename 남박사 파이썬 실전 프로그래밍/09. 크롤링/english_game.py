import requests
from bs4 import BeautifulSoup

url = "https://www.usatoday.com"
r = requests.get(url)
bs = BeautifulSoup(r.text, "lxml")
lists = bs.select("div.gnt_m_th > a")
for li in lists:
    href = url + li["href"]
    print(href)

    r = requests.get(href)
    bs = BeautifulSoup(r.text, "lxml")
    texts = bs.select("div.gnt_ar_b > p.gnt_ar_b_p")
    contents = [p.text for p in texts]
    # 리스트 컴프리헨션
    # contents = []
    # for p in texts:
    #     contents.append(p.text)
    print(contents)