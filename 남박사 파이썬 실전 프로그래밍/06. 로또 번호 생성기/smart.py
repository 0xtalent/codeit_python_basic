'''
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자리수 만큼 연속 숫자를 포함하는 번호를 생성하는 기능
'''

import numpy

def make_lotto_number(**kwargs):
    # range 값 중에 6개를 중복되지 않게 만들어라, 리스트 형태로 담김
    rand_number = numpy.random.choice(range(1, 46), 6, replace=False)
    rand_number.sort()

    # 최종 로또 번호가 완성될 변수
    lotto = []

    # **kwargs 키워드 인자로 파라미터를 준 이유는 사용자가 옵션을 줄수도 있고 안줄수도 있어서
    if kwargs.get("include"):
        include = kwargs.get("include")
        # extend 시켜줘야 확장됨 append 쓰면 [[1, 2, 3]] 됨
        lotto.extend(include)

        cnt_make = 6 - len(lotto)

        for _ in range(cnt_make):
            for j in rand_number:
                if lotto.count(j) == 0:
                    lotto.append(j)
                    break

    else:
        lotto.extend(rand_number)

    return lotto

print(make_lotto_number(include=[1, 2]))
