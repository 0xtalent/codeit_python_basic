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

"""

# 해주신 피드백
"""
잘하셨습니다!!!^^
지금과 같이 values(), keys()를 다 구할 수도 있겠지만,
keys()만으로도 같은 결과를 낼 수 있을 것입니다.
수강기간 여유도 있으시니 추가과제라 생각하시고 이를 개선하여 제출 부탁드려요:)
"""

# 재도전

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

# 무한으로 즐겨요 명륜진사갈비

while True:
    random_numbers = randint(0, len(word_jang_keys) - 1)

    # 질문하기
    guess = input("{}: ".format(word_jang_keys[random_numbers]))

    # q면 종료, 정답 오답 체크
    if guess == 'q':
        break
    elif guess == word_jang[word_jang_keys[random_numbers]]:
        print("정답입니다. 당신은 천재")
    else:
        print("오답입니다. 당신은 바보. 정답은 {}".format(word_jang[word_jang_keys[random_numbers]]))

# 데이터 누수 방지
word_list.close()

# 앜ㅋ randint(0, 5) 가 4까지 인줄 알았네ㅋㅋㅋ이거 그거 아니야
# 아 그리고 20분 고민한 듯, word_jang["word_jang_keys[random_numbers]"]
# 이렇게 했는데 안되서 한참 고민했는데 "" 없애니까 되네...
# 이유는 word_jang_keys[random_numbers] 이게 나올 때 "어쩌구"로 나올 듯?

# 2019-11-27 채점결과
"""
키 값을 접근하는 건 방법은 맞습니다^^
그런데 "word_jang_keys[random_number]" 와 같이 쓴다면 이것은 문자열입니다.
word_jang 에 "word_jang_keys[random_number]" 라는 key 가 있어야 하는 것이죠.
word_jang_keys[random_number] 라고 쓴 이유는 key로만 이루어진 리스트의 인덱스를
활용하기 위함이므로 변수의 쓰임 형태인 word_jang_keys[random_number]
이렇게만 써주셔야 할 것입니다^^
"""

# 정답은?
"""
from random import randint

# 파일 열기
in_file = opne('vocabulary.txt', 'r')

# 사전 만들기
vocab = {}

for line in_file:
    # 정보 정리
    data = line.strip().split(" ")
    english_word = data[0]
    korean_word = data[1]

    # 사전에 추가
    vocab[english_word] = korean_word

while True:
    keys = list(vocab.keys())
    index = randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab(english_word)

    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))

    # 정답 확인
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))

# 파일 닫기
in_file.close()

"""
