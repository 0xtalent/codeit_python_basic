# Chapter05-2
# 제어문

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 피보나치 수열
# 피보나치 수열의 첫 20개 항을 차례대로 출력

# 상수
COUNT = 20

# 변수
previous = 0
current = 1
i = 0

while i < 20:
    print(current)
    temp = previous
    previous = current
    current = temp + current
    i += 1

# 1 1 2 3 5 8 13 21
# 알고리즘 공부가 중요한 것 같다.

# 출제자의 설명
# 피보나치 수를 구하기 위해서는 마지막 두 값을 더해야 합니다.
# 그렇기 때문에 어떤 경우에도 마지막 두 값은 알고 있어야겠죠.
# 이걸 current라는 변수에 가장 마지막 값을 저장해 두고
# previous라는 값에 마지막에서 두번째 값을 저장해 두겠습니다.
# 피보나치수열에서 첫번째 값과 두번째 값은 모두 1이기 때문에
# 일단은 current를 1로 두고 previous는 0으로 두겠습니다.
# 그리고 현재까지 몇 개의 피보나치 수를 출력했는지는 i라는 변수에 넣겠습니다.
# 아직까지는 한 개도 없기 때문에 0으로 시작합니다.
# 그리고 이제 반복문을 써야됩니다.
# COUNT의 수만큼 반복하고 싶으니까 "while i는 COUNT 보다 작다" 이렇게 쓰면 되고요
# 수행부분에는 print(currnet)를 쓰면 됩니다.
# 그리고나서 current랑 previous를 새로운 값들로 바꿔줘야 되는데
# ...이 문제를 해결하기 위해서 temp라는 다른 변수를 만들어줍니다.
# 첫 번째 줄에서 temp라는 변수를 만들고 그 변수에 previous의 값을 저장합니다.

# 오케이 이해 갔어. previous를 current로 대체
# current는 current + temp로 대체
# previos는 temp에 저장

print()

# 구구단
# i = 1
# j = 2
#
# while i < 9:
#     i = i + 1
#     while j < 9:
#         j = j + 1
#         print(i * j)

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print("%d * %d = %d" % (i, j, i * j ))
        j += 1
    i += 1
# 겨우 풀었네...
# i += 1, j += 1 어디에 두어야 하는지 계속 고민했네
# print 위에 i += 1, j += 1 놓기도 하고
# print 아래에서 i += 1, j += 1 동일한 위치에 놓기도 하고
# 순서도 바꿔보고 했지만...계속 틀렸지...
# i += 1 을 한 탭 앞으로 빼니까 맞네...
# 알고리즘적 사고를 통해서 만들어야 하는데
# 아직은 그게 부족해...
# 해설 보면서 공부하자...

# 해설
# 자 이제 그러면 i를 1부터 9까지 반복해야 되는데
# 그 뜻은 i가 1일 경우에 while문이 있어야 되고, i가 2일 경우에 while문이 있어야 되고
# i가 3일 경우에 반복문이 있어야 되고, 이렇게 해야 1단부터 9단까지 다 출력이 되겠죠
# 그러면 j반복문을 i반복문 안에 넣어주면 됩니다.
# 이렇게 반복문 안에 반복문이 있는 걸 네스티드 반복문이라고 합니다.

# 아 알았다. i 반복문 안에 j 반복문을 넣어준 거구나
# 그러니까 i += 1, j += 1 위치 고민할 필요도 없구나
# 그리고 j = 1 위치가 중요한데, 이건 순서도 생각해보면 답나옴
# 다시 j = 1 되야 되니까 위치를 맨 위가 아니라 i 반복문 안에 넣어줘야지

# break문
# 만약 while문의 조건부분과 상관 없이 반복문에서 나오고 싶으면 break문을 쓰면 됩니다.

# continue문
# 만약 현재 진행되고 있는 수행부분을 중단시키고
# 바로 조건부분을 다시 확인하고 싶으면 continue문을 쓰면 됩니다.

i = 0
while i < 15:
    i = i + 1

    # i가 홀수면 print(i) 안하고 바로 조건부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)
