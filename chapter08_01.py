# Chapter08-1
# for문과 리스트 심화

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

"""
for 반복문과 range 함수 정리

for문과 while문이 할 수 있는 것들은 거의 똑같은데, 특정 상황에 따라 for문을 쓰면
while문을 쓰는 것보다 코드가 더 깔끔할 수 있습니다.

과자들 = ["베베", "포카칩", "자갈치", "프링글스", "와클"]

i = 0
while i < len(과자들):
    print(과자들[i])
    i = i + 1

while 문에서 i는 인덱싱을 위한 용도, 즉 리스트의 값들을 받아오기 위한 정도지
그 외에는 아무 쓸모다 없죠. for문이 이 while문보다 깔끔한 경우가 바로
리스트의 인덱스가 필요없을 때입니다.

이번에는 똑같은 일을 하는 프로그램을 while문 대신 for문으로 써보겠습니다.

과자들 = ["베베", "포카칩", "자갈치", "프링글스", "와클"]

for 과자 in 과자들:
    print(과자)

for문도 while문처럼 반복적으로 이 수행부분이 실행되는데요
while문과 달리 조건 부분이 없죠

여기 과자는 이 for문의 수행부분에서만 쓰이고 사라지는 로컬변수인데요.
처음 수행부분으로 들어갈 때는 과자들 리스트에 0번 인덱스의 값, 베베죠
그리고 그 다음 들어갈 때는 과자들 리스트의 인덱스 1의 값...
이렇게 리스트의 마지막까지 계속 반복하고 끝납니다.

range 함수

파라미터가 2개 있는 range 함수
for i in range(n, m):
    print(i)

파라미터가 1개 있는 range 함수
for i in range(1, 11):
    print(i)

파라미터가 3개 있는 range 함수
for i in range(3, 17, 3):
    print(i)
"""

# range 연습

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# 인덱스와 원소 출력
for i in numbers:
    print(numbers.index(i), i)

# 출제자는 이렇게 했네
for i in range(len(numbers)):
    print(i, numbers[i])

# 거듭제곱
# 2의 n제곱의 결과값을 출력하는 프로그램을 만드세요.

for i in range(11):
    print("2^{} = {}".format(i, 2**i))

# 이건 좀 잘했다는 생각이 드든 군
# 살짝 실수 range(10) 한점 i*i 한점ㅋㅋ 2**i 겠죠ㅎㅎ
# for문도 잘썼고, 문자열 포맷팅도 잘했고, 거듭제곱도 잘썼고
# 나 자신 칭찬해

# for문으로 구구단
# 예전에 했던 구구단 프로그램을 이번에는 while문 대신 for문을 써서 만들어보세요

for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j))

# 와 미친 나 한번에 성공함
# 재능있나?
# 알고리즘이 중요한 것 똑같은데
# 정보처리기사 알고리즘, 순서도가 계속 생각나
# 기업에서 코딩테스트를 보는 이유가 있어
# 더 열심히 하자 ! 의대생처럼 공부!!

# 피타고라스 수
