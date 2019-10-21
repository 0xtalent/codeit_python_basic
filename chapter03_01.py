# Chapter03-1

# 추상화(Abstraction): 복잡한 세부사항을 숨기고, 주요한 기능에만 집중할 수 있게 해주는 개념
# 변수(Variable), 함수(Function), 객체(class)

# 지정 연산자(Assignment Operator)

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

name = "Elon Musk"
nationality = "USA"
phone_number = "112"

print("Hi, my name is {}. I'm from {} My phone number is {}.".format(name, nationality, phone_number))
print("Hi, my name is %s. I'm from %s" % (name, nationality))
print("My phone number is %s" % (phone_number))

# 함수 정리

# 변수가 값을 보관하는 역할을 한다면, 함수(function)는 명령들을 보관하는 역할을 합니다.
# def 함수이름(파라미터):
#     실행할 문장 1
#     실행할 문장 2
#     실행할 문장 3

# print_full_name 함수 정의
def print_full_name(first_name, last_name):
    print(last_name, ",", first_name)

# 테스트 코드
print_full_name("하용", "정")

# 인공지능이 원하는 정답은
def print_full_name(first_name, last_name):
    print("%s, %s" % (last_name, first_name))

print_full_name("하용", "정")

# 거스름돈 계산기
def calculate_change(payment, cost):
    # 총 거스롬돈 계산 후, 50000원 짜리 몇 장이 필요한지 계산.
    change = payment - cost
    fifty_thousand_count = int(change / 50000)

    # 50000원 짜리 지폐로 거슬러준 후 남은 거스롬돈 계산, 10000원 짜리 몇 장이 필요한지 계산.
    change = change % 50000
    ten_thousand_count = int(change / 10000)

    # 10000원 짜리 지폐로 거슬러준 후 남은 거스롬돈 계산, 5000원 짜리 몇 장이 필요한지 계산.
    change = change % 10000
    five_thousand_count = int(change / 5000)

    # 5000원 짜리 지폐로 거슬러준 후 남은 거스롬돈 계산, 1000원 짜리 몇 장이 필요한지 계산.
    change = change % 5000
    one_thousand_count = int(change / 1000)

    print("50000원 지폐: {}장".format(fifty_thousand_count))
    print("10000원 지폐: {}장".format(ten_thousand_count))
    print("5000원 지폐: {}장".format(five_thousand_count))
    print("1000원 지폐: {}장".format(one_thousand_count))

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

# 추상화 꿀팁
# 자주 쓰이는 표현을 더 간략하게 쓸 수 있게 해주는 문법을 syntactic sugar라고 합니다.
# 파라미터의 기본값을 설정해두면 함수 호출을 할 때 파라미터에 해당되는 값을 넘겨주지 않았을 경우, 그 파라미터는 기본값을 갖게 됩니다.
# 이런 파라미터를 optional parameter라고 부릅니다.
# Optional parameter는 모두 마지막에 있어야 합니다.
