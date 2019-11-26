# 프로젝트: 로또 당첨기

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from random import randint

# 무작위로 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    box = []
    while len(box) < 6:
        random_number = randint(1, 45)
        while random_number in box:
            random_number = randint(1, 45)
        box.append(random_number)
    return sorted(box)

# generate_numbers를 이용해서 6개 숫자를 뽑고 보너스 숫자 1개 더 뽑기
def draw_winning_numbers():
    draw_numbers = list(generate_numbers())
    while len(draw_numbers) < 7:
        random_number = randint(1, 45)
        while random_number in draw_numbers:
            random_number = randint(1, 45)
        draw_numbers.append(random_number)
    return draw_numbers

# 두 리스트에서 중복되는 숫자가 몇 개인지 구하기
def count_matching_numbers(list1, list2):
    matching_number = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if list1[i] == list2[j]:
                matching_number += 1
    return matching_number

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    if count_matching_numbers(numbers, winning_numbers) == 6:
        return 1000000000
    elif count_matching_numbers(numbers, winning_numbers) == 5:
        for k in range(0, 5):
            if numbers[k]== winning_numbers[6]:
                return 50000000
    elif count_matching_numbers(numbers, winning_numbers) == 5:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers) == 3:
        return 5000
    else:
        return 0

# else가 없으니까 오류나네
