# 남박사01-2
# 2019-11-27
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 파이썬 집합
a = {1, 2, 3}
print(type(a))
# 집합은 중복을 허용하지 않습니다.
b = set([0, 0, 0, 1, 2, 3])
print(b)

a.add(7)
print(a)

a.remove(3)
print(a)
#
