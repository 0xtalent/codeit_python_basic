# 프로젝트: 로또 당첨기

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
"""
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
"""
# 2019-11-27 채점결과
"""
잘하셨습니다!!👍🏻 아래 피드백을 확인해주세요:)
1. generate_numbers 함수의 반환값이 이미 리스트인데, list()를 쓸 필요는 없지 않을까요?
2. i, j 와 같은 변수명은 아쉽습니다. 변수명은 항상 신경을 써주시기 바랍니다^^
3. count_matching_numbers 함수는 좀 더 간결한 구현이 가능할 것 같습니다. 링크를 참고해보시면 좋겠습니다^^
4. 과제 조건에 의하면 count_matching_numbers 함수는 리스트 길이에 상관없이
리스트 두개가 주어지면 모든 인덱스를 순회하여 일치하는 갯수를 반환해야 합니다.
그렇다면 어떻게 구현해야 할까요? 만약 보너스 번호를 제하기 위해서 위와 같이 구현하셨더라도
range 범위는 다시 생각해보시면 좋겠습니다^^
5. check 함수내에서 count_matching_numbers 함수를 매 조건마다 호출할 필요가 있을까요?
한번만 호출할 수도 있을 것입니다.
6. count_matching_numbers 함수가 과제 조건대로 구현된다면 이미 아실 것 같지만
check 함수에서 문제가 생길 것입니다. [1,2,3,4,5,6], [1,2,7,8,9,10, 3] 이 numbers 와
winning_numbers 로 주어질 경우 5등에 당첨이 되는 것이죠. 이를 어떻게 해결할 수 있을까요?
충분히 생각을 해보시고 잘 떠오르지 않으신다면 링크를 참고해보셔도 좋습니다^^
이를 개선해보시고 제출 부탁드려요:)
"""

# 재도전
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
    draw_numbers = generate_numbers()
    while len(draw_numbers) < 7:
        random_number = randint(1, 45)
        while random_number in draw_numbers:
            random_number = randint(1, 45)
        draw_numbers.append(random_number)
    return draw_numbers

# 두 리스트에서 중복되는 숫자가 몇 개인지 구하기
def count_matching_numbers(list1, list2):
    matching_number = 0
    for number1 in range(0, 5):
        for number2 in range(0, 5):
            if list1[number1] == list2[number2]:
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
