# Chapter06-1
# 모듈

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 모듈 정리

# 모듈(module)이란 변수, 함수, 클래스 등을 모아 놓은 파일입니다.
# 모듈에 정보를 한번만 정의해두면 여러 프로그램에서 쉽게 가져다 쓸 수 있습니다.

# from 모듈 파일의 이름 import 불러올 변수/함수/클래스
# *를 쓰면, 모듈 안에 정의된 모든 변수/함수/클래스를 불러올 수 있습니다.

# randint는 두 정수 사이의 어떤 랜덤한 정수(난수)를 리턴시켜주는 함수입니다.
# from random import randint

# uniform은 random이라는 모듈 안에 정의되어 있는,
# 두 수 사이의 랜덤한 소수(난수)를 리턴시켜주는 함수입니다.

# input 함수 정리

# name = input("이름을 입력하세요: ")
# print("Hello " + name)

# 숫자 맞추기 게임

from random import randint

ANSWER = randint(0, 9)
sido = 4

# answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(sido)))
# while sido <= 4:
#     if answer == ANSWER:
#         print("축하합니다. {}번만에 숫자를 맞추셨습니다.".format(sido))
#         break
#     else:
#         if answer > ANSWER:
#             print("Up")
#             sido -= 1
#         else:
#             print("Down")
#             sido -= 1
#
# print("아쉽습니다. 정답은 {}였습니다.".format(ANSWER))

# answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(sido)))
# while sido >= 1:
#     if answer == ANSWER:
#         print("축하합니다. {}번만에 숫자를 맞추셨습니다.".format(sido))
#         break
#     elif answer > ANSWER:
#         print("Up")
#         sido -= 1
#     else:
#         print("Down")
#         sido -= 1
#
# print("아쉽습니다. 정답은 {}였습니다.".format(ANSWER))

# ㅋㅋ 이래 놓고 왜 안되나 고민했네 바본가

# while sido >= 1:
#     answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(sido)))
#     if answer == ANSWER:
#         print("축하합니다. {}번만에 숫자를 맞추셨습니다.".format(sido))
#         break
#     elif answer < ANSWER:
#         print("Up")
#         sido -= 1
#     else:
#         print("Down")
#         sido -= 1
#
# if sido == 0:
#     print("아쉽습니다. 정답은 {}였습니다.".format(ANSWER))

# 아 sido 실수 했잖아요

while sido >= 1:
    answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(sido)))
    if answer == ANSWER:
        print("축하합니다. {}번만에 숫자를 맞추셨습니다.".format(5-sido))
        break
    elif answer < ANSWER:
        print("Up")
        sido -= 1
    else:
        print("Down")
        sido -= 1

if sido == 0:
    print("아쉽습니다. 정답은 {}였습니다.".format(ANSWER))

# 채점 피드백
# 1. sido 와 같이 한글발음으로 이루어진 영단어보다는 tries라든지
# 온전한 영어단어로 써주시면 좀 더 좋은 선택이 될 것 같습니다:)
# 2. sido -= 1이 중복되는데 한번만 쓸 수도 있지 않을까요?
# 3.(5 - sido)와 같이 한칸 띄어 써주시면 더 좋은 코드가 될 것입니다.
# 이 부분만 다시 한번 확인해보시고 해설을 참고해주세요:) 수고하셨습니다^^

# 출제자님은 어떻게 푸셨는지

"""
from random import randint

# 상수
NUM_TRIES = 4
ANSWER = randint(1, 20)

# 변수
tries = 0
guess = -1

# 시도가 남았고 아직 답을 못 맞췄을 경우
while tries < NUM_TRIES and guess != ANSWER:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (NUM_TRIES - tries)))
    tries = tries + 1

    if guess < ANSWER:
        print("Up")
    elif guess > ANSWER:
        print("Down")

# while 반복문에서 나오게 되면 두 가지 경우가 있습니다.
# 답을 맞춰서 나왔거나 아니면 그 시도가 이제 더 이상 남지 않아서 나왔거나

if guess == ANSWER:
    print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (tries))
else:
    print("아쉽습니다. 정답은 %d였습니다." % (ANSWER))

"""
