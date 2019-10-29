# fastcampus03-1
# 리스트

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

"""
시퀀스(Sequence): 순서가 있는 자료형
파이썬에는 리스트, 튜플, 문자열 등이 있다.

리스트 왜 쓰지? 여러개의 자료를 하나의 변수로 관리할 때 사용
*비어있는 리스트는 list(), []로 생성 가능

담기는 담았는데 어떻게 쓰지?
시퀀스 타입의 객체들은 인덱스 연산을 통해 내부 항목에 접근 가능

문자열과 마찬가지로 슬라이싱도 가능
var.append 도 가능
연산도 가능
특정한 위치에 넣기도 가능 var1.insert(1, 어쩌고)
삭제도 가능 var1.remove(어쩌고), del var1[0]
"""

# 튜플
"""
리스트와 거의 비슷하나, 정의 후 항목들의 수정, 삭제가 불가능하다.
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3, 4
t5 = 1,
* 튜플의 요소가 한개일 땐 콤마를 붙여야 한다.

튜플을 정의할 때 괄호가 없어도 무관하지만
괄호로 묶는게 튜플임을 구분하기 좋다.

수정도 안되고 삭제도 안되는 튜플 언제 쓰나?
튜플 언패킹
"""
c1 = "red"
c2 = "blue"
colors = c1, c2
print(type(colors))
print(c1, c2)
c1, c2 = c2, c1
print(c1, c2)
