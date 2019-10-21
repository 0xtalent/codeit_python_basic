# Chapter05-1
# 제어문

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# while문을 사용하여 1 이상 100 이하의 짝수를 출력
i = 0
while i <= 100:
    print(i)
    i = i + 2

print()

# while문을 사용하여 100 이상의 자연수 중 가장 작은 23의 배수를 출력
i = 100
while i % 23 != 0:
    i += 1
print(i)

# if/elif/else
# while문은 반복문(loop)
# if문은 조건문(conditional)

# 학점 계산기
def print_grade(midterm, final):
    total = midterm + final
    if total >= 90:
        print("You get an A")
    elif total >= 80:
        print("You get a B")
    elif total >= 70:
        print("You get a C")
    elif total >= 60:
        print("You get a D")
    else:
        print("You fail")

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

# 이상한 수학 문제 1
# 100이하의 자연수 중 8의 배수이지만, 12의 배수는 아닌 것을 모두 출력

i = 1
while i <= 100:
    if i % 8 == 0:
        if i % 12 != 0:
            print(i)
    i += 1

print()

# 이상한 수학 문제 2
# 1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력
i = 1
sum = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        sum = sum + i
    i += 1
print(sum)

# 흠...i 위치하고 print 위치 때문에 몇번 틀렸는데 말이야
# 논리적으로 생각해보면 답이 나오는데...
# i는 while 안에서 반복해줘야 되고
# print는 다 끝나고 밖에서 찍는게 맞기
# sum은 if문 안에서 돌리는게 맞고(처음에 sum 선언도 안함ㅋ)
# 더 꼼꼼하게 생각하자

# 약수 찾기
# 자연수 중 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력

n = 120
i = 1
count = 0
while i <= n:
    if n % i == 0:
        print(i)
        count += 1
    i += 1

print("{}의 약수는 총 {}개 입니다.".format(n, count))

# 택이의 우승상금

# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE = 1100000000

# 변수 정의
year = 1988
amount = 50000000

# while year <= 2016:
#     if amount > APARTMENT_PRICE:
#         amount = amount * (1 + INTEREST_RATE)
#         year += 1
#         print("동일 아저씨의 말씀이 맞습니다.")
#     else:
#         print("미란 아주머니의 말씀이 맞습니다.")

while year < 2016:
    amount = amount * (1 + INTEREST_RATE)
    year += 1
if amount > APARTMENT_PRICE:
    print("{0:.0f}원 차이로 동일 아저씨의 말씀이 맞습니다.".format(amount - APARTMENT_PRICE))
else:
    print("{0:.0f}원 차이로 미란 아주머니의 말씀이 맞습니다".format(APARTMENT_PRICE - amount))

# while 하고 if를 연결하려는 이상한 생각을 가지고 있었네
# 논리적으로 생각하면 답이 나온다
# 프로그래밍은 단순해 제대로 생각하면 답 나온다
# 네가 이상하게 생각할 뿐, 서투르게 생각할 뿐
# 게을러지기 위해서 치열하게 노력하자
