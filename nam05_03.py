# 남박사05-3
# 2019-12-02 11:26

# 파이썬 데코레이터
# 이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념

# 파이썬에서 함수는 일급객체
# 클로저 사용
# 함수내 함수를 정의할 수 있음

def outer_function(msg):
    def inner_function():
        return "난 내부 함수인데 {} 메세지를 받았어".format(msg)
    return inner_function

c = outer_function("헬로")
print(c.__closure__[0].cell_contents)