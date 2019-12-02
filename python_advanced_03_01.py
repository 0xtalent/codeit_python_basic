# Chapter03-1
# 파이썬 심화
# 시퀀스 형
# 컨테이너(Container) : 서로 다른 자료형을 저장 할 수 있는 것[list, tuple, collections.deque]
# Flat : 한 개의 자료형만 저장할 수 있는 것[str, bytes, bytearray, array.array, memoryview]
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists

chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s))

# Comprehending Lists
codes2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x : x > 40, map(ord, chars)))

print('EX1-1 -', codes1)
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)
print('EX1-5 -', [chr(s) for s in codes1])
print('EX1-6 -', [chr(s) for s in codes2])
print('EX1-7 -', [chr(s) for s in codes3])
print('EX1-8 -', [chr(s) for s in codes4])
print()

# Generator

import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)

# Array
array_g = array.array('I', (ord(s) for s in chars))

print('EX2-1 -', tuple_g)
print('EX2-2 -', next(tuple_g))
print('EX2-3 -', next(tuple_g))
print('EX2-4 -', array_g)
print('EX2-4 -', array_g.tolist())
print()

# 제너레이터 예제

print('EX3-1 -', ('%s' % c + str(n) for c in ['a', 'b', 'c', 'd'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['a', 'b', 'c', 'd'] for n in range(1, 11)):
    print('EX3-2 -', s)

print()

# 리스트 사용할 때 주의할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print('EX4-1 -', marks1)
print('EX4-2 -', marks2)
print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-1 -', marks1)
print('EX4-2 -', marks2)

# 증명
print('EX4-5 -', [id(i) for i in marks1])
print('EX4-6 -', [id(i) for i in marks2])
print()

# Tuple advanced

# Packing & Unpacking


print('EX5-1 -', divmod(100, 9))
print('EX5-2 -', divmod(*(100, 9)))
print('EX5-3 -', *(divmod(100, 9)))
print()

x, y, *rest = range(10)
print('EX5-4 -', x, y, rest)
x, y, *rest = range(2)
print('EX5-5 -', x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print('EX5-6 -', x, y, rest)
print()

# Mutable(가변) vs Imutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print('EX6-1 -', l, m, id(l), id(m))

l = l * 2
m = m * 2

print('EX6-2 -', l, m, id(l), id(m))

l *= 2
m *= 2

print('EX6-3 -', l, m, id(l), id(m))

# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 '새로운' 객체 반환(원본은 그대로)

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))
print('EX7-3 -', sorted(f_list, key=len))
print('EX7-4 -', sorted(f_list, key=lambda x:x[-1]))
print('EX7-5 -', sorted(f_list, key=lambda x:x[-1], reverse=True))

print('EX7-6 -', f_list)
print()

# sort : 정렬 후 객체 직접 변경
# None을 반환 했다는 것은 객체를 직접 변경했구나

print('EX7-7 -', f_list.sort(), f_list)
print('EX7-8 -', f_list.sort(reverse=True), f_list)
print('EX7-9 -', f_list.sort(key=len), f_list)
print('EX7-10 -', f_list.sort(key=lambda x: x[-1]), f_list)
print('EX7-11 -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)