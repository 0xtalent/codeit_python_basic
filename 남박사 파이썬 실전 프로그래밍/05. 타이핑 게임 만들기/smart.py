'''
한글 = ((초성 * 21) + 중성) * 28 + 종성 + 44032

초성 = ((x - 44032) / 28) / 21
중성 = ((x - 44032) / 28) % 21
종성 = (x - 44032) % 28
'''

import time
import random
import os

CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅛ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "뵤", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

# print(len(CHO))
# print(len(JUNG))
# print(len(JONG))

# a = chr(((0 * 21) + 0) * 28 + 0 + 44032)
# print(a)

def break_korean(string):
    word_list = list(string)
    break_word = []

    for k in word_list:
        if ord(k) >= ord("가") and ord(k) <= ord("힣"):
            # 유니코드 상 몇번째 글자인지 인덱스를 구한다.
            char_index = ord(k) - ord('가')

            # 초성 = ((문자코드 - 44032) / 28) / 21
            char1 = int((char_index / 28) / 21)
            break_word.append(CHO[char1])

            # 중성 = ((x - 44032) / 28) % 21
            char2 = int((char_index / 28) % 21)
            break_word.append(JUNG[char2])

            # 종성 = (x - 44032) % 28
            char3 = int(char_index % 28)

            if char3 > 0:
                break_word.append(JONG[char3])
        
        else:
            break_word.append(k)
    return break_word

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

    src = break_korean(q)
    tar = break_korean(user_input)

    if user_input == "/exit":
        break

    correct = 0
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if c == src[i]:
            correct += 1
    tot_len = len(src)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = (correct / end_time) * 60

    print("속도: {:0.2f} 정확도: {} 오타율: {}".format(speed, c, e))
    os.system("pause")