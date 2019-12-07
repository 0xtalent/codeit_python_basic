# 남박사07-1
# 2019-12-07 18:17

# 숫자 야구게임 만들기(파이썬 기초, 랜덤 함수, 반복문, 조건문)

import random
import os

numbers = []
number = str(random.randint(0, 9))

for i in range(3):
    while number in numbers:
        number = str(random.randint(0, 9))
    numbers.append(number)

os.system("cls")

print("*" * 60)
print("야구 게임을 시작합니다!!")
print("*" * 60)

count_strike = 0
count_ball = 0

while count_strike < 3:
    count_strike = 0
    count_ball = 0

    num = str(input("숫자 3자리를 입력하세요>"))
    if len(num) == 3:
        # 사용자하고 정답하고 비교해야 하니까 2중 for문
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j:
                    count_strike += 1
                elif num[i] == numbers[j] and i != j:
                    count_ball += 1
        if count_strike == 0 and count_ball == 0:
            print("삼진 아웃!")
        else:
            output = ""
            # 서로 각각 다른 조건이어서 if문 두번
            if count_strike > 0:
                output += "{} 스트라이크".format(count_strike)
            if count_ball > 0:
                output += " {} 볼".format(count_ball)
            
            print(output.strip())
print("게임 성공!")