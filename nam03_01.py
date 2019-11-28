# 남박사03-1
# 2019-11-28
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 사용자 입력 받기
user = input("사용자 이름을 입력하세요")
print(user)

# 입력한 숫자가 소수인지 알아보기

while True:
    num = input("2 이상의 숫자를 입력하세요> ")
    if not num.isnumeric():
        continue
    num = int(num)
    if num < 2:
        continue
    break

# isprime = True
# for n in range(2, num):
#     if num % n == 0:
#         isprime = False
#         break
#
# if isprime:
#     print("소수입니다.")
# else:
#     print("소수가 아닙니다.")

# 다른 방식
prime_list = [False, False] + [True] * (num - 1)
primes = []

for i in range(2, num + 1):
    if prime_list[i]:
        for j in range(2 * i, num + 1, i):
            prime_list[j] = False

primes = [i for i in range(2, num + 1) if prime_list[i] == True]
print(primes)

if num in primes:
    print("소수 입니다.")
else:
    print("소수가 아닙니다.")

# 와 어렵다 근데 환상적이다.
