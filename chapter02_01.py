# Chapter02-1

# 연산 부호 (Operators)

# +	덧셈 (addition)
# -	뺄셈 (subtraction)
# *	곱셈 (multiplication)
# /	나눗셈 (division)
# %	나머지 (modulo)
# ** 거듭제곱 (exponentiation)

# 정수형 (Integer)

# 소수형 (Floating Point)

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("'응답하라 1988'은 많은 시청자들에게 사랑을 받은 드라마에요.")
print('데카르트는 "나는 생각한다. 고로 존재한다."라고 말했다.')

# 문자열 포맷팅(String Formatting)
# %d 정수(Integer)
# %f 소수(Floating point)
# %s 문자열(String)

wage = 5                  # 시급 (1시간에 5달러)
exchange_rate = 1142.16   # 환율 (1달러에 1142.16원)

print("{}시간에 {}달러 벌었습니다.".format(5, wage * 5,))
print("{}시간에 {}원 벌었습니다.".format(1, wage * 1 *  exchange_rate))
print("%d시간에 %.1f%s 벌었습니다." % (5, wage * 5 * exchange_rate, "원"))

# // 연산자는 나눗셈 연산 후 결과값을 내림 합니다.
# 즉 소수부분을 버리고 정수부분만 남겨둡니다.
# 이걸 floor division이라고 부릅니다.

# round는 소수형을 반올림해줍니다.
print(round(1.421, 1))      # 1.421을 소수점 1째 자리로 반올림

# 줄바꿈 기호 (Newline Character)
# 문자열 내에 \n 기호는 줄을 바꾸어주는 역할을 합니다.
# 키보드의 엔터키와 동일한 효과입니다.
print("안녕하세요\n정하용입니다\n딥러닝 개발자가\n되고싶어요")
