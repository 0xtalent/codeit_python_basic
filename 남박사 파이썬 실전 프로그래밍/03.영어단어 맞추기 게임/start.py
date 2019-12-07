# 남박사08-1
# 2019-12-07 21:00

# 영어 단어 맞추기 게임(파이썬 기초, 랜덤 함수, 반복문, 조건문. 딕셔너리)

import random

words_dict = {
    "사자": "lion",
    "호랑이": "tiger",
    "사과": "apple",
    "비행기": "airplane"
}

# 딕셔너리는 순서의 개념이 없기때문에 순서를 만들어주기위해 리스트에 담자
words = []

for word in words_dict:
    words.append(word)

random.shuffle(words)

chance = 3
for i in range(0, len(words)):
    q = words[i]
    for j in range(0, chance):
        user_input= str(input("{}의 영어 단어를 입력하세요".format(q)))
        english = words_dict[q]

        if user_input.strip().lower() == english.lower():
            print("정답입니다!")
            break
        else:
            print("틀렸습니다.")
    if user_input != english:
        print("정답은 {}였습니다.".format(english))

print("모든 문제를 다 푸셨네요. 다음에 또만나요 안녕!")
