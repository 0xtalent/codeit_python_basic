# fastcampus05-1
# fileIO, exception, git, process, thread

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

10:18
"""
