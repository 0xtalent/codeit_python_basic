# 남박사04-1
# 2019-11-28
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 파이썬 내장 함수
import math
a = math.isclose(0.1 + 0.2, 0.3)
print(a)

a = "홍길동, 김길동, 가가멜"

b = a.split(",")
print(b)

c = dir(str)
print(c)
