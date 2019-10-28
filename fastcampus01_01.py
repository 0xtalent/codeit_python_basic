# fastcampus01-1
# 코드잇 잠시 멈추고 듣고 있던 패스트 캠퍼스 강의 듣기

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def exam_arg(*args):
    print(args)
    print(args[1])
    print(type(args))

exam_arg('test', '출력', 123)

"""
가변 위치인자를 사용할 땐 값이 tuple 형태로 전달된다.
tuple은 iterable 객체이니 순회, 인덱스로 조회가 가능

가변 위치인자를 받을 땐 *만 붙이면 된다.
다만 관용적으로 args라고 붙여서 사용

그러면 가변 키워드 인자도 받을 수 있겠죠?
가변 키워드 인자는 *이 두개입니다.
**kwargs
"""
print()

def exam_kwarg(**kwargs):
    print(kwargs)
    print(type(kwargs))

exam_kwarg(key = 'test', word = '출력', args = 123)

"""
가변 키워드 인자를 사용할 땐 값이 dictionary 형태로 전달됩니다.

가변 인자들 또한 보통의 위치 인자, 키워드 인자의 규칙과 동일합니다.
키워드 인자는 위치 인자보다 무조건 뒤에 와야 함
"""

# docstring

print(print.__doc__)

"""
함수를 실행하기 위해 어떻게 사용해야 하는지 적혀있다.
특별한 문서를 따로 첨부하지 않아도 된다는 말
우리가 만든 함수에도 적을 수 있다.

함수를 작성할 때 선언 바로 다음 줄에 써야 한다.
만약 함수 선언 바로 다음줄에 쓰지 않고 중간에 쓰게되면
파이썬은 docstring이 아니라 그저 문자열로 인식함.
"""
def exam_docstring(*args):
    """
    울랄라
    """
print(exam_docstring.__doc__)

# 오늘 배운 거 정리
# 가변인자: 가변 위치 인자(*), 가변 키워드 인자(**), docstring
