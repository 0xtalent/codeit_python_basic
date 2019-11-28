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

rfile = open("sample.txt", mode="r", encoding="utf-8")
content = rfile.read()
rfile.close()

print(content)

"""
with open("sample.txt", mode="r", encoding="utf-8") as file:
    print(file.read())
"""
