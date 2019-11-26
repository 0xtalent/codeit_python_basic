# Chapter09-1
# 데이터 분석 101

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 단어 퀴즈 문제
word_list = open('vocabulary.txt', 'r', encoding = 'utf-8' )

for line in word_list:
    data = line.strip().split(": ")
    english_word = data[0]
    korean_word = data[1]

    guess = input("{}: ".format(data[0]))

    if guess == data[1]:
        print("증답입니다.")
    else:
        print("틀렸네영. 정답은 {}인디;;".format(data[1]))

word_list.close()

# 해주신 피드백
"""
잘하셨습니다!!👍🏻
9, 14번째 줄에서도 6, 7번째 줄의 변수를 활용할 수 있지 않을까요?
이 부분만 한번 생각해보시고 해설을 참고해주세요^^
수고하셨습니다:)
"""

# 아하 변수 설정해 놓고 왜 사용을 안했지ㅋㅋ
