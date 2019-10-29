# fastcampus05-1
# recursive_function, class

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# recursive_function

"""
보통 재귀호출을 설명할 때 피보나치 수열, 하노이의 탑, 유클리드 호제법 등을 예로들어 설명
일반적인 프로그램을 만들때는 많이 쓰이지 않는다.
재귀호출로 푸는 것들 대부분은 반복문으로 처리가 가능하기 때문. 반복문이 효율도 좋다.

재귀함수에서 중요한 건 두가지. 재귀조건, 탈출조건
탈출조건이 없다면 재귀를 무한히 반복하다 오류를 발생시킴
* 무한루프에 빠진다. 그리고 stack overflow가 발생

재귀호출을 실전에서는 어디서 쓸까?
예외처리를 할 때 사용
"""
def input_answer():
    try:
        your_input = int(input("정답을 입력해주세요:"))
        return your_input
    except:
        return input_answer

# class

"""
절차지향 프로그래밍: C언어, 코볼, 포트란 등
수 많은 지식인들이 느낀 불편함과 고찰로 탄생한 것이 객체지향 프로그래밍
객체지향 프로그래밍이란 객체(object)단위로 데이터와 기능(function)을 하나로 묶어 쓰는 방식
파이썬 또한 객체지향 프로그래밍을 지원한다. class 예약어를 통해

class란?
속성(attribute)과 동작(method)를 갖는 데이터 타입
attribute = 클래스 내부에서 선언된 변수
method = 클래스 내부에서 선언된 함수

클래스 문법에 대해서 ARABOZA
클래스는 self라는 특별한 의미의 인수를 받는다.
무조건 첫번째로 받아야 한다.
*self는 자기 자신을 의미

self는 메서드를 호출하는 객체 자신이 자동으로 전달된다.
클래스의 메서드를 사용할 때 어떤 객체가 해당 메서드를 사용하고 있는지 알기 위함이며
하나의 메서드를 여러 객체가 사용할 수 있게끔 하기 위해서이다.

__init__은 생성자라고 부르며 initualize 객체를 만들 때 호출된다.
말 그대로 객체를 초기화 한다.
self 이후에 매개변수를 추가로 받으면 객체를 초기화할 때 값을 입력받을 수 있다.

하나의 클래스로부터 생성된 객체들이 같은 값을 가지게 하고 싶다면
생성자(__init__) 밖에다 적어주세요
"""
class MySon:
    description = "귀여운내새끼"
    def __init__(self, name, age, kind, distinct, speak):
        self.name = name
        self.age = age
        self.kind = kind
        self.distinct = distinct
        self.speak = speak

    def bark(self):
        print(self.speak)

"""
만들 줄 알면? 쓸 줄도 알아야 한다.
클래스 내부에서 속성(attribute)에 접근할 땐 self.속성의 형식으로 접근할 수 있다.
*메서드(method) 또한 self.메서드의 형식으로 접근 가능
"""

cloud = MySon("구름", "6month", "mix", "very cute", "야옹")
print(cloud.name)
print(cloud.age)
print(cloud.kind)
print(cloud.distinct)
cloud.bark()

# class 어렵네 개념은 이해 가는데, 실제 프로그램 만들 때 쓸 수는 없어. 더 공부하자

"""
우리가 이때까지 사용한 자료형(list, int, str) 등도 사실은 클래스다.
바꿔말하면 객체다.

파이썬은 모든 것이 객체로 이루어져 있다고 할 수 있을 만큼 객체지향적으로 작성되어 있다.
"""
print(dir(list))

"""
상속이라는 기능은 객체지향 프로그래밍에서 아주 중요한 기능 중 하나
코드의 중복을 막을 수 있으며(재활용)
상속을 받은 하위클래스의 공통적인 규약(메서드)을 만들기 위함(유지보수 용이, 통일성)

상속을 받은 하위클래스(자식)을 만드는 이유는
객체(데이터)들의 고유한 특성(정보, 동작 등)을 다루기 위함
쉽게 말하면 "여기까지는 똑같아야 하는데 여기부터는 달라야 해"

하위 클래스에 있는 메서드를 사용하는 것 = 메서드 오버라이드(덮어쓰기)

이 밖에도 클래스에는 더 많은 기능과 테크닉이 존재한다.
다중상속, property, setter, static method...
"""

# 클래스 어렵다
# 남박사, 코드잇으로 복습하고
# 파이썬 심화 인강 듣고
# 인프런, 각종 패스트캠퍼스 인강으로 계속 공부하기
