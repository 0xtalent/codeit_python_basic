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

# 피타고라스 수 문제

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a +  b * b == c * c and a < b < c:
            print(a * b * c)

# Aliasing(Alias: 가명)

# 리스트 뒤집기 문제
"""
numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
for i in numbers:
    temp = i
    i = len(numbers) - i - 1
    len(numbers) - i - 1 = i
print("뒤집어진 리스트: " + str(numbers))
#
# temp?
"""
numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
for left in range(int(len(numbers) * 1/2)):
    temp = numbers[left]
    numbers[left] = numbers[len(numbers) - left - 1]
    numbers[len(numbers) - left - 1] = temp

print("뒤집어진 리스트: " + str(numbers))

# 좋은 팁

# left가 리스트 전체의 길이의 범위로 지정되어있어서,
# 전반부의 원소와 후반부의 원소가 한 번 교체된 후, 또 다시 교체되어 원 상태로 돌아온 것입니다.
# left의 범위를 리스트 길의의 절반으로 제한해주어야 합니다.

# 실수 한 거
# 위치값 지정해 주기 위해서 range 함수 써서 해결해야 했었는데
# 이상하게 하려 했음

# 리스트와 문자열 정리
"""
인덱싱 (Indexing)
두 자료형은 공통적으로 인덱싱이 가능합니다.

for 반복문
두 자료형은 공통적으로 인덱싱이 가능합니다. 따라서 for 반복문에도 활용할 수 있습니다.

슬라이싱 (Slicing)
두 자료형은 공통적으로 슬라이싱이 가능합니다.

len 함수
두 자료형은 모두 길이를 재는 len 함수를 쓸 수 있습니다.

Mutable (수정 가능) vs. Immutable (수정 불가능)
하지만 차이점이 있습니다. 리스트는 데이터를 바꿀 수 있지만,
문자열은 데이터를 바꿀 수 없다는 것입니다.
리스트와 같이 수정 가능한 자료형을 'mutable'한 자료형이라고 부르고,
문자열과 같이 수정 불가능한 자료형을 'immutable'한 자료형이라고 부릅니다.
숫자, 불린, 문자열은 모두 immutable한 자료형입니다.
"""
print()
# 자리수 합 구하기 문제

# 자리수 합 리턴
def sum_digit(num):
    str_num = str(num)
    sum = 0
    for i in str_num:
        sum = sum + int(i)
    return(sum)

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
i = 1
j = 0
while i <= 1000:
    j += sum_digit(i)
    i += 1
print(j)

# 정답
"""
for문으로 했넹

total = 0
for i in range(1, 1001):
    total = total + sum_digit(i)
print(total)
"""

# 주민등록번호 가리기 문제

def mask_security_number(security_number):
    return(security_number[0: - 4] + "****")

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

print()

# 필린드롬 문제
# 모르겠엉 너무 어려웡
# 정답은 뭘까? 바로 해설 ㄱㄱ

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
