# 남박사03-2
# 2019-11-28
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 파이썬에서 파일 읽고 쓰기

file = open("sample.txt", mode="w", encoding="utf-8")
file.write("hello python")
file.close()

# 파일 사용 후 close() 하지 않으면 다른 프로그래밍 및 객체에서 접근하지 못하는 현상이 생길 수 있습니다.

rfile = open("sample.txt", mode="r", encoding="utf-8")
content = rfile.read() # readline: 한줄씩 읽기
rfile.close()

print(content)

"""
with open("sample.txt", mode="r", encoding="utf-8") as file:
    print(file.read())
"""