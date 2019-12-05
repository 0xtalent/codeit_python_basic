# Chapter12-1
# 2019-12-05 17:00
# 코드잇 프로그래밍 기초 남은거 빠르게 끝내기

# 재귀 함수

# 숫자 합 문제(팩토리얼이랑 똑같네)

# 1부터 n까지의 합을 리턴
def triangle_number(n):
    if n == 1:
        return 1
    if n > 0:
        return triangle_number(n - 1) + n

# 완벽한 정답은?
def triangle_number2(n):
    if n == 1:
        return 1
    return triangle_number(n - 1) + n

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))

# 피보나치 수열 문제

# n번째 피보나치 수를 리턴
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))

# 더 이쁘게는
# n번째 피보나치 수를 리턴
def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)