# 남박사01-1

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 이스케이프 문자

print("\\")

"""
\n 줄바꿈
\t 탭
\\ 역슬래쉬
\' 따옴표
\" 쌍따옴표
"""

# 문자열 인덱싱&슬라이싱

a = "test python string"
print(a[-1])
print(a[0:10])

# 문자열 포맷팅
