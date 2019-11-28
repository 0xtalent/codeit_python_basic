# 남박사03-3
# 2019-11-28
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 파이썬 예외 처리 try / except

# val = "10.5"
# n = int(val)

# try:
#     val = "10.5"
#     n = int(val)
# except Exception as e:
#     print("{} 오류 발생".format(e))

try:
    n = "10"
    v = int(n)
except Exception as e:
    print("{} 오류 발생".format(e))
else:
    print("정상")
finally:
    print("오류가 발생하거나 말거나 finally 실행")
