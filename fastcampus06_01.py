# fastcampus06-1
# fileIO, exception, git

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

"""
프로그램이 실행되는 동안 데이터는 휘발성 기억장치인 메모리(RAM)에 저장된다.
작업중인 데이터를 저장하거나, 저장되어 있는 데이터를 불러오기 위해선
하드디스크, SSD와 같은 보조기억장치에 파일을 쓰거나, 읽는 과정이 필요하다.
* 혹은 별도의 저장공간

파일을 읽거나, 쓰기 위해선 먼저 파일을 열어야 하겠죠
파이썬에서는 이러한 기능들을 사용하고자 open()이라는 내장함수를 만들어주었다.
"""
f = open("some.txt", "w")
for i in range(1, 9 + 1):
    data = "5*{} = {} \n".format(i, 5 * i)
    f.write(data)
f.close()

"""
파일을 쓰는 법은 알겠으니, 작성한 텍스트 파일을 파이썬에서 읽어들이고 싶다면?
"""

f = open("some.txt", "r")
print(f.read())
f.close()

"""
read()함수를 통해 텍스트 파일 전체를 문자열로 가져온다
전체를 가지고 와서 메모리에 저장하기 때문에 메모리 사용에 유의해야 한다.
*파일 내용이 너무 크면 메모리에 다 안들어간다.
"""

# 줄 단위로 읽기

f = open("some.txt", "r")
while True:
    data = f.readline()
    if not data:
        break
    print(data, end = "")
f.close()

"""
readline 함수를 통해 텍스트 파일을 한줄 씩 읽는다.
readline 함수는 더 이상 읽을 줄이 없다면 None을 반환하며,
조건문을 통해 while문을 탈출
"""

f = open("some.txt", "r")
data = f.readlines()
f.close()
for line in data:
    print(line, end = "")

"""
readlines()함수(readline과 다름!!)는 텍스트 파일의 모든 라인을 읽어서
줄 단위로 요소를 가지는 리스트로 반환합니다.
그 리스트를 반복문을 통해 읽는 것

open(파일이 존재하는 경로와 파일명, 모드, 인코딩)
파일을 열땐 모드라는 게 존재한다.
파일이 열릴 때 작업하고자 하는 모드로 열어줘야 한다.
당연히 작업하고자 하는 모드와 맞지 않는 작업을 하게되면 에러가 난다.

r 읽기모드
w 쓰기모드
x
a
...
"""

# 최소한으로 필기하며 빠르게 공부하기

# 예외처리(Error Handling)

"""
파이썬에서는 이러한 상황에서 유연하게 대처하고자
try-except라는 예약어를 제공한다.

try:
    시도할 코드
except:
    에러 발생시 실행할 코드

else도 가능
fonally문은 try문을 수행 도중 예외의 발생 여부와 상관없이 무조건 수행
에러가 나도 실행이 안나도 실행. DB connection이나 열린 파일 등을 닫아야 할 때
close() 해서 리소스를 회수해야 할 때 주로 사용

custom error도 가능
"""

# git

"""
리눅스 토발즈가 개발한 분산형 버전 관리 시스템(VCS)
VCS(Version Control System)란?
동일한 정보에 대한 여러 버전을 관리하는 프로그래밍 세계에서는 소스코드

토발즈는 버전 관리 시스템으로 Bitkeeper를 쓰며 리눅스를 개발하고 있다가
여러 이념들의 충돌과 성능에 화가나서 2주만에 버전 관리 시스템 Git을 만들어버림ㅋ

git의 특징
빠른 속도, 단순한 구조
분산형 저장소 지원
비선형적 개발(브랜치를 나누어 개발) 가능

코드 백업
저장소를 통한 협업

소스코드를 주고 받지 않아도 동시작업이 가능 -> 생산성 증가
수정내용을 commit 단위로 관리, 원하는 시점으로 돌아가기 가능 -> 백업
branch 단위로 개발하여 A를 개발하던 도중 B라는 기능 추가 가능 -> 편안한 테스트 가능
인터넷이 없어도 개발이 가능 -> 장소제약이 없어짐

git config --global user.username ""
git config --list
git remote add origin https://~
git push -u origin master

reset
revert
log
status

branch란?
분기점을 생성하고 동일한 소스코드에서 다른 개발을 하기 위한 활동
git은 처음 세팅을 할 때 master라는 branch를 기본값으로 만들어 줍니다.

git branch <branch이름>
git checkout <branch이름>

merge: 두개의 branch의 코드를 합쳐주는 기능
git merge <합칠branch>
merge를 실행하면 현재 branch에 합쳐진다.

git checkout master
git merge login_logic

conflict
"""
