# 남박사01-1
# 2019-11-26
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 이스케이프 문자

print("\\")

"""
\n 줄바꿈
\t 탭
\\ 역슬래쉬
\' 따옴표
\" 쌍따옴표
"""

# 문자열 인덱싱&슬라이싱

a = "test python string"
print(a[-1])
print(a[0:10])

# 문자열 포맷팅

# 2019-11-27
# 문자열 메서드
test = "가나다라마바사아 abcdefgh"
print(test.find("zz"))

path = "c:\\test\\abcd\\abcd.jpg"
print(path.split("\\"))

# .upper, .lower
# .isalpha
# .islower

print(dir(str))

# 파이썬 데이터 구조
"""
append() 리스트 추가
insert() 리스트 삽입
del 인덱스 삭제
remove(요소) 삭제
.pop(인덱스) 삭제 및 값 리턴
a.extend(b) 리스트 확장
a.sort 정렬
a.reverse 역정렬
1 in a
"""

# 파이썬 튜플, tuple()
a = 1, 2, 3, 4, 5
print(type(a))
"""
﻿튜플은 값을 변경하거나 삭제 할 수 없습니다.
패킹: 튜플로 만드는 작업
언패킹: 튜플에서 값을 꺼내는 작업
"""
a1, a2, a3, a4, a5 = a
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

# 딕셔너리
b = {}
print(type(b))
c = {"과자" : "먹고싶다", "사탕": "먹기싫다."}
print(c.get("과자"))
print(c.get("치킨"))

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

# 형변환 casting
