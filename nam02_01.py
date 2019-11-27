# 남박사02-1
# 2019-11-27
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 조건문
# 반복문
a = [(1, 2), (3, 4), (5, 6)]
for i in a:
    for j in i:
        print(j)

# for문을 쓰는데 인덱스 값을 써야 할 때 enumerate
msg = "Python programming"

for s, i in enumerate(msg, start=1):
    print(s, i)

# 리스트 컴프리헨션
# result = []
# for num in range(1, 6):
#     result.append(num + 5)
# print(result)

result = [num + 5 for num in range(1, 6)]
print(result)

for i in range(2, 10):
    for j in range(1, 10):
        result = i * j
        print("{} x {} = {}".format(i, j, result))

gugudan = ["{} x {} = {}".format(i, j, i * j) for i in range(2, 10) for j in range(1, 10)]
print(gugudan)

# 
