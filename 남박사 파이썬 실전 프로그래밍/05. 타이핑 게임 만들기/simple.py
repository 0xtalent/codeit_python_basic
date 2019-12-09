# 타이핑 게임 만들기

import time
import random
import os

word_list = [
    "2019년 EBS에서 제작한 유튜브 채널 자이언트 펭TV의 주인공으로 남극에서 온 펭귄이다.",
    "'자이언트 펭TV'는 평일 저녁 어린이 예능인 생방송 톡!톡! 보니하니의 한 코너였으나",
    "EBS는 2019년 가을 개편에서 '자이언트 펭TV'를 별도 프로그램으로 독립시켜",
    "금요일 저녁 8시 30분에 편성했다."
]

random.shuffle(word_list)

for q in word_list:
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    if user_input == "/exit":
        break

    correct = 0
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]:
            correct += 1
    tot_len = len(q)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = (correct / end_time) * 60

    print("속도: {:0.2f} 정확도: {} 오타율: {}".format(speed, c, e))
    os.system("pause")