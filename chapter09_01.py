# Chapter09-1
# 데이터 분석 101

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

"""
# 파일 읽기 정리

파일을 읽기 위해서는 open 내장 함수를 쓰면 됩니다.

in_file = open('chicken.txt', 'r')

for문에 쓰면 in_file을 마치 문자열 리스트(list of strings)처럼 다룰 수 있습니다.

for line in in_file:
    print(line)

연 파일은 꼭 닫자
파일을 열면 프로그램이 실행되는 동안 메모리를 차지하고 있는데,
close 메소드를 쓰면 메모리를 해방시켜줄 수 있습니다.

in_file.close()
"""

"""
# strip 정리
strip 메소드는 문자열의 가장 앞쪽과 뒤쪽에 있는 화이트 스페이스(white space)가
제거된 새로운 문자열을 리턴해줍니다.

print(" \n\t   Hello world!   \n\n\t\n  ".strip())

하지만 strip은 문자열의 가장 앞쪽과 뒤쪽에 있는 화이트 스페이스만 제거하지,
중간 중간 있는 화이트 스페이스는 그대로 둔다는 것을 기억합시다.

print(" \n\t   Hello      wo\nrld!   \n\n\t\n  ".strip())
"""

"""
# split 정리

split 메소드는 파라미터로 넘겨주는 값을 기준으로 문자열을 분리시키고,
분리된 값들이 정리되어 있는 리스트를 리턴해줍니다.

print("1. 2. 3. 4. 5. 6".split("."))

그런데 인덱스 1의 값부터는 숫자 앞에 띄어쓰기가 하나씩 있습니다.
기존의 문자열을 보면 두 숫자 사이에는 점과 띄어쓰기(". ")가 모두 있기 때문이죠.
문제를 고치기 위해서는 파라미터를 "." 대신 ". "를 넘겨주면 됩니다.

print("1. 2. 3. 4. 5. 6".split(". "))

파라미터가 없는 경우

사실 split메소드의 파라미터는 옵셔널 파라미터입니다.
아무 값도 넘겨주지 않았을 경우 기본값으로 ""가 넘어가게 됩니다.
그러면 공백(화이트 스페이스)을 기준으로 문자열을 나누게 되는거죠.

print("1 2 3 4 5 6".split())

화이트 스페이스는 띄어쓰기 뿐만 아니라 탭과 엔터를 모두 포함
"""

# 코딩에 빠진 닭
#
# amount = 0
# days = 0
#
# in_file = open('data/chicken.txt', 'r')
#
# for line in in_file:
#     data = line.strip().split(": ")
#     amount = amount + int(data[1])
#     days += 1
#
# print(amount / days)
#
# in_file.close()

# strip과 split을 스스로 섞어 쓸 수 있을까?

# 2019-11-25

# 파일쓰기
"""
out_file = open('new_file.txt', 'w')
그리고 파일에 쓰려면 out_file에 write 메소드를 불러주면 됩니다.
엔터를 치기 위해서는 Newline Character("\n") 넣어주는 것도 잊지 마시고요.
그리고 파일을 읽을 때와 마찬가지로 파일을 다 쓰면 꼭 닫아주는 것이 좋습니다.
out_file.close()
"""

# 단어장 만들기 문제
import codecs
# 파일 쓸수있게 open
out_file = codecs.open('vocabulary.txt', 'w')

# q가 입력되기 전까지 ㄱㄱ
while True:
    english_word = input("영어 단어를 입력하세요: ")
    if english_word == "q":
        break
    else:
        korean_meaning = input("한국어 뜻을 입력하세요: ")
        out_file.write("{}: {}\n".format(english_word, korean_meaning))
