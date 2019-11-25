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
