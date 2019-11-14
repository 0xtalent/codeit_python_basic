# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    """
    Student class
    Author: Jung Hayong
    Data: 2019.11.13
    """

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str {}',format(self._name)

    def __repr__(Self):
        return 'repr {}',format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1

# Self 의미
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
studt2 = Student('Chang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'superhayong@naver.com')

# ID 확인
print(id(studt1))
print(id(studt2))

# dir & __dict__ 확인

print(dir(studt1))
print(dir(studt2))

print()
print()

print(studt1.__dict__)
print(studt2.__dict__)

# Docstring

print(Student.__doc__)
print()

# 실행
studt1.detail_info()
studt2.detail_info()

"""
클래스는 속성과 메소드로 이루어진다.
속성에서 인스턴스 변수는 내꺼
클래스 변수는 모두가 공유한다
"""
