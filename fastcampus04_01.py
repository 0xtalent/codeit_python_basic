# fastcampus03-1
# iterator, generator, CLI

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# iterator

x_range = range(1, 100 + 1)
x_list = ["a", "b", "c", "d", "e"]
x_set = {1, 2, 3, 4, 5}
x_str = "iterable"

# print(next(x_range))

"""
iterable한 객체를 iterator로 바꾸고 싶다면 iter()함수를 사용해라

근데 이런거 없이도 순회 잘 했잖아요?
list, str같은 iterable한 object를 사용할 때 굳이 iter()를 쓰지 않아도
for문으로 요소를 조회할 수 있었습니다.
그 이유는 for문이 순회하는 동안 팡썬 내부에서 임시로 iterble 객체들을
iterator로 자동 변환을 해주었기 때문
"""
x_list = iter(x_list)
print(type(x_list))
print(next(x_list))
print(next(x_list))
print(next(x_list))
print(next(x_list))
print(next(x_list))

# generator

"""
iterator를 생성해주는 함수
그래서 어쨌다는 거죠?

generator를 사용하면 memory를 효율적으로 사용할 수 있습니다.

iterator는 가지고 있는 모든 요소를 메모리에 저장하기 때문에
iterator의 크기만큼 메모리의 사용량이 늘어납니다.
generator는 데이터를 한번에 메모리에 저장하는게 아니라
next()함수를 통해 차례대로 접근할 때마다 메모리에 저장
generator는 진짜 계싼 결과값이 필요하기 전까지 계산을 하지 않는다.

"""
import sys
print(sys.getsizeof([i for i in range(1, 10000 + 1)]))
print(sys.getsizeof((i for i in range(1, 10000 + 1))))

# 잘 모르겠다ㅎㅎ

"""
정리하면 Iterator:
연속적인 데이터를 나타내는 객체
iterable한 객체를 순회하기 위해선 iter()내장함수가 필요

Generator: Iterator 생성기, 게으른 연산, 효율적인 메모리 사용
"""

# 쉘(shell)
"""
사용자의 명령을 해석하고 커널에 요청하는 역할
*커널을 보호한다는 의미

CLI: Command Line Interface(명령 줄 인터페이스)
GUI: Graphic User Interface(그래픽 사용자 인터페이스)

CLI: bash, csh, zsh
GUI: 윈도우 탐색기, finder

pwd: 현재 디렉토리 위치
cd: 이동할 경로
ls: 목록
ipconfig
ifconfig
ping
Commandmkdir
...
"""

# VIM 에디터

"""
VI Improved
개선된 VI

VI: Visual Editor UNIX 계열 운영체제에서 사용하는 텍스트 에디터 중 하나
리눅스나 유닉스 환경에선 대부분 내장되어 있다.
"""
