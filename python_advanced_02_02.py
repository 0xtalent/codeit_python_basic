# Chapter02-2
# 파이썬 심화
# Special Method(Magic Method)

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 매직 메소드 실습
# 파이썬의 중요한 핵심 프레임 워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 매직메소드 기초 설명

# 기본형
print(int)

# 모든 속성 및 메소드 출력
print(dir(int))
print()

n = 100

# 사용
print('EX1-1 -', n + 200)
print('EX1-2 -', n.__add__(200))
print('EX1-3 -', n.__doc__)
print('EX1-4 -', n.__bool__(), bool(n))
print('EX1-5 -', n * 100, n.__mul__(100))
print()

# 클래스 예제1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info : {}, {}'.format(self._name, self._height)

    def __ge__(self, x):
        print("진짜 호출됨 >> __ge__ Method.")
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print("진짜 호출됨 >> __le__ Method.")
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print("진짜 호출됨 >> __sub__ Method.")
        return self._height - x._height

# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

# 매직 메소드 출력
print("EX2-1 -", s1 >= s2)
print("EX2-2 -", s1 <= s2)
print("EX2-3 -", s1 - s2)
print("EX2-4 -", s2 - s1)
print("EX2-5 -", s1)
print("EX2-6 -", s2)
print()
