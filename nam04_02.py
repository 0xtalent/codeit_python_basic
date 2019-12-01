# 남박사04-1
# 2019-11-28 18:55
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 사용자 함수

c = 10 # 전역변수

def add(a, b):
    """docstring
    """
    c = a + b # 지역변수
    return c

# 매개변수, 파라메타, 파람, 인자값 등 여러가지 단어로 표현
# 함수에 인풋 데이터를 전달하기 위한 변수

def save_winner(*args):
    print(args)

save_winner("방구", "낄낄낄", "퍄퍄퍄")
# args는 튜플로 넘어오네

def save_winner2(**kwargs):
    print(kwargs)
    if kwargs.get("name1"):
        print(kwargs["name1"])

save_winner2(name1="라라라", name2="뵤뵤뵤")

# 궁금한거 있어요... 왜 여기서 "name1" 이렇게 넣어야 하죠...
# 그러면 문자열 아닌가요... 변수를 넣어야 하는거 아닌가요...

# 함수를 변수에 담을 수 있다!
def hi():
    print("안녕!")

hi()
hello = hi
hello()
print(type(hello))

# def add(a, b):
#     return a + b

# 인자로 함수를 담기, 아 어려워ㅋㅋ
def cal(func, a, b):
    print("결과 {}".format(func(a, b)))

cal(add, 1, 5)

# 함수 안에 함수를 선언도 가능!
