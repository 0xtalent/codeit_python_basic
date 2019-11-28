# 남박사03-4
# 2019-11-28
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 유니코드와 인코딩
a = '가'
# 유니코드 10진수 값
print(ord(a))

# 16진수 값
print(hex(ord(a)))
