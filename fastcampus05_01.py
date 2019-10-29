# fastcampus05-1
# recursive_function, class, fileIO

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
"""
