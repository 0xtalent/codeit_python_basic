# 남박사09-1
# 2019-12-07 21:15

# 콘솔 스마트 계산기 만들기 심플-파이썬 기초, 계산기 로직, 리스트, 반복문, eval 함수

import os

while True:
    os.system("cls")
    s = input("계산식 입력> ")
    print("결과: {}".format(eval(s)))
    os.system("pause")