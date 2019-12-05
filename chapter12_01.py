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

# 재귀 함수 문제

# # n의 각 자릿수의 합을 리턴
# def sum_digits(n):
#     n = str(n)
#     if len(n) == 1:
#         return n
#     return n[0] + sum_digits(n[1:])

# # 테스트
# print(sum_digits(22541))
# print(sum_digits(92130))
# print(sum_digits(12634))
# print(sum_digits(704))
# print(sum_digits(3755))

# 바보야? 안되서 고민하다가
# 문자열로 바꿔야되지만, 더해야되니까 다시 정수형으로...

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    return int(n[0]) + sum_digits(n[1:])

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 완벽한 정답은?

# n의 각 자릿수의 합을 리턴
def sum_digits2(n):
    if n < 10:
        return n
    else:
        str_n = str(n)
        return int(str_n[0]) + sum_digits(int(str_n[1:]))

"""
일단 파라미터로 받는 n이 정수형이기 때문에 쓰기 쉽게 문자열로 변환시켜줬습니다. 
그리고 첫번째 숫자(str_n[0])와 나머지 숫자들(str_n[1:])의 합(sum_digits)을 더해준 
결과값을 리턴시켜줬습니다.
"""

# 리스트 뒤집기 문제

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    if len(some_list) < 2:
        return some_list
    return flip(some_list[1:]) + some_list[:1]

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 대박 쫌 어렵다...