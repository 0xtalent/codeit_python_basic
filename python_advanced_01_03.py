# Chapter01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

class Student(object):
    """
    Student class
    Author : Jung
    Date : 2019.11.15
    Description : Class, Static, Instance Method
    """
    # Class Variable
    tuition = 1.0

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
            return '{}, {}.format'(self._first_name, self._last_name)

        # Instance Method
        def detail_info(self):
            return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

        # Instance Method
        def get_fee(self):
            return 'Before Tuition -> ID : {}, fee : {}'.format(self._id, self._tuition)

        # Instance Method
        def get_fee_culc(Self):
            return 'After Tuition -> ID : {}, fee : {}'.format(self._id, self._tuition * Student.tuition)

        def __str__(self):
            return 'Student Info -> name: {} grade: {} email: {}'.format(self.full_name(), self._grade, self._email)

student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student2@naver.com', '2', 500, 4.3)

print(student_1)
print(student_2)
