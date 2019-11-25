# Chapter09-1
# 데이터 분석 101

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 사전 정리
"""
사전이 리스트와 가장 다른 점은 key가 정수뿐만 아니라 아무 자료형이나 될 수 있다는 것
"""

# 사전 활용법
"""
여기서 key들만 모두 받으려면 keys 메소드를 쓰면 됩니다.
print(family.keys())

value들을 모두 받기 위해서 values 메소드를 쓰면 됩니다.
print(family.values())

그리고 family의 value들을 리스트로 쓰고 싶으면 list 함수로 형 변환을 하면 됩니다.
family_values = list(family.values())
"""

# 고급 단어장 문제

from random import randint
word_list = open('vocabulary.txt', 'r', encoding = 'utf-8')

# dict 만들기
word_jang = {}

# vocabulary.txt의 값을 불러와서 각각 생성한 dict에 입력하기
for data in word_list:
    line = data.strip().split(" ")
    korean_word = line[0]
    english_word = line[1]
    word_jang[korean_word] = english_word

# 리스트로 변환하기
word_jang_keys = list(word_jang.keys())
word_jang_values = list(word_jang.values())

# 무한으로 즐겨요 명륜진사갈비

while True:
    random_numbers = randint(0, len(word_jang_keys) + 1)

    # 질문하기
    guess = input("{}: ".format(word_jang_keys[random_numbers]))

    # q면 종료, 정답 오답 체크\
    if guess == 'q':
        break
    elif guess == word_jang_values[random_numbers]:
        print("정답입니다. 당신은 천재")
    else:
        print("오답입니다. 당신은 바보. 정답은 {}".format(word_jang_values[random_numbers]))

# 데이터 누수 방지
word_list.close()
