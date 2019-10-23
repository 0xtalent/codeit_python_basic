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
