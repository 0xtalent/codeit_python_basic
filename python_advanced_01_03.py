# Chapter01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 기본 인스턴스 메소드

class Student(object):
    """
    Student class
    Author : Jung
    Date : 2019.11.15
    Description : Class, Static, Instance Method
    """
    # Class Variable
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{}, {}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> ID : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After Tuition -> ID : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # Instance Method
    def __str__(self):
        return 'Student Info -> name: {} grade: {} email: {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print("더 큰 수를 입력해라")
            return
        cls.tuition_per = per
        print("인상되었습니다")


# 학생 인스턴스
student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student2@naver.com', '2', 500, 4.3)

# 기본 정보 출력
print(student_1)
print(student_2)
print()

# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보(등록금 인상 전)
print(student_1.get_fee())
print(student_2.get_fee())

print()
# 학비 인상(클래스 메소드 미사용)
# Student.tuition_per = 1.2

Student.raise_fee(1.2)

# 학비 정보(등록금 인상 후)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
