# Chapter04-1
# 추상화 심화

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# return문은:

# 함수 호출 부분(function call)을 return문 뒤에 오는 값으로 대체합니다.
# 현재 함수의 실행을 멈추고 함수가 호출된 지점으로 돌아가서 진행됩니다.

def f(x):
    print("f 시작")
    return x + 1
    print("f 끝") # 절대 실행 안됨. Dead code

print(f(2))
print()

# return vs. print
def print_square(x):
    print(x * x)

print(print_square(3))

print()
# print(print_square(3))의 경우 우선 print_square 함수에 있는
# print(x * x)에 의해 9가 출력됩니다.
# 그리고 함수 호출 부분은 함수의 리턴값으로 대체되는데,
# print_square 함수의 리턴값은 None입니다.
# 따라서 None도 함께 출력됩니다.

def secret_number():
    print("우리의 비밀 번호는: ")
    return 486

print(secret_number())

# 파이썬은 (1)~(3)번 줄의 함수 정의를 건너뛰고, (5)번 줄에 도착합니다.
# (5)번 줄에서 secret_number()라는 함수 호출 때문에, 파이썬은 secret_number 함수가 정의되어 있는 (1)번 줄로 이동합니다.
# (2)번 줄의 print 명령에 따라 파이썬은 "우리의 비밀 번호는: "을 출력합니다.
# 486을 리턴하라는 명령이 있기 때문에
# 함수의 실행이 중단되고,
# 함수를 호출한 secret_number()라는 부분이 486으로 대체됩니다.
# (5)번 줄의 print(secret_number())는 print(486)과 동일해져서 486이 출력됩니다.

# 만일 위 코드에서 (5)번 줄이 print(secret_number())가 아닌, secret_number()였으면 어땠을까요?
def secret_number():
    print("우리의 비밀 번호는: ")
    return 486

secret_number()

# 그렇다면 함수 내부에서 print문과 return문의 순서가 바뀌어 있으면 어떻게 될까요?
def secret_number():
    return 486
    print("우리의 비밀 번호는: ")

print(secret_number())

# local 변수와 global 변수
# 여러 함수에서 통일된 global 변수를 쓰면
# 한번의 실수로 프로그램 전체에 영향을 줄 수 있습니다.
# global 변수를 꼭 써야하는 상황인지 신중하게 생각해보고 쓰셔야합니다!

# 상수 정리
# global 변수의 가장 자연스럽고 좋은 예시는 상수입니다.
# 상수(constant)는 프로그램 내내 바뀌지 않는 값을 의미합니다.

# 스타일 가이드
# 모든 변수와 함수 이름은 소문자로 써주시고, 여러 단어일 경우 _로 나눠주세요.
# 모든 상수 이름은 대문자로 써주시고, 여러 단어일 경우 _로 나눠주세요.
# 의미있는 변수/함수 이름으로 설정
# 글 쓸때 문단을 나누듯이 프로그램을 짤때도 엔터키를 써서 적당히 나눠주세요.
# 적당한 추상화
# 적당한 코멘트
# 적당한 줄 길이: 한 줄에 80자를 넘기지 맙시다.

# 짝수? 홀수?

def is_evenly_divisible(number):
    if number % 2 ==0:
        return True
    else:
        return False

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))

# 출제자가 원했던 답은?
def is_evenly_divisible(number):
    return number % 2 == 0
