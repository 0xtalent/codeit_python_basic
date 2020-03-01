# 200301 08:48 다시 복습하는 중
# 강의 끝까지 완강 & 복습
# 열심히 공부, 모든 것을 공부
# 파이썬 주니어 개발자 되자!!!

'''
크롤링 하는 방법
1. 원하는 웹 페이지에 접속하여 HTML 데이터를 받아온다.
2. 받아온 HTML 데이터를 분석가능한 형태로 가공한다.
3. 원하는 데이터를 추출한다.
'''

import  requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

response = requests.get("https://www.naver.com")

# print(response.status_code)
# print(response.headers)
# print(response.text)
# response.content는 디코딩 되기 전인 바이너리 형태의 데이터고
# 디코딩이 된 상태의 데이터는 text로 접근할 수 있습니다.

# bs = BeautifulSoup(response.text, "html.parser") # 요 텍스트 데이타를 html.parser를 통해 html텍스트를 분석해준다.
# for img in bs.select("img"):
#     print(img)

session = HTMLSession()
response = session.get("https://www.naver.com")
print(response.html.links)