# Chapter07-1
# 리스트

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#  리스트 정리
# 리스트(list)라는 자료형을 쓰면 하나의 변수만으로도 여러 개의 정보를 저장할 수 있습니다.

# 인덱싱 (Indexing)
# print(numbers[0])
# print(names[-1])

# 슬라이싱 (Slicing)
# print(numbers[0:4])
# print(numbers[0:-3])

# 리스트 인덱싱 연습
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
a = 0
while a <= 6:
    print(greetings[a])
    a += 1

# 정답인지 아닌지 잘 모르겠지만 했었던 실수
# a 초깃값 지정 안함
# .pop() 으로 어떻게 해보려고 함

# 출제자가 원하는 정답은?
# greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
#
# i = 0
# while i < len(greetings):
#     print(greetings[i])
#     i = i + 1

# < <= 차이가 있나?

# 리스트 함수 정리

# len 함수는, 리스트 안의 원소 개수를 세주는 역할을 합니다.
# print("리스트의 길이는: %d" % len(alphabet))
#
# insert와 append를 사용하여 리스트에 원소를 추가할 수 있습니다.
# numbers.append(5)
# numbers.insert(3, 12)

# del 함수를 사용함으로써 원하는 리스트의 원소를 삭제할 수 있습니다.
# del numbers[4:]
#
# sorted 함수는 리스트의 원소들을 오름차순으로 정렬한 새로운 리스트를 리턴해줍니다.
# numbers = sorted(numbers)
#
# 리스트들을 +로 연결할 수 있습니다.
# alphabet = alphabet1 + alphabet2


# 온도 단위 바꾸기 문제

# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환
# while sample_temperature_list == []:
#     fahrenheit_to_celsius(sample_temperature_list)
# 원소 하나하나씩 바꾸는 방법 말고 이런식으로 할 수는 없나...ㅋ
a = 0
while a < len(sample_temperature_list):
    sample_temperature_list[a] = fahrenheit_to_celsius(sample_temperature_list[a])
    a += 1

# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(sample_temperature_list))


# 환전 서비스 문제

# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    return won * 1/1000

# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):
    return dollars * 125

# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))

# amounts를 원(￦)에서 달러($)로 바꿔주기
a = 0
while a < len(amounts):
    amounts[a] = krw_to_usd(amounts[a])
    a += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔(￥)으로 바꿔주기
b = 0
while b < len(amounts):
    amounts[b] = usd_to_jpy(amounts[b])
    b += 1

# 엔(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))


# 리스트 함수 활용하기 문제

# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
i = 1
while i < 11:
    numbers.append(i)
    i += 1
print(numbers)

# numbers에서 홀수 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        i += 1

# 짝수여서 제거되지 않을 때에만 i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
# 바보 처음에 numbers[0] = 20 이랬다
# 다음에 append 씀 그랬더니 하나의 아규먼트만 받는다네ㅋㅋ
print(numbers)

# numbers를 정렬해서 출력
numbers = sorted(numbers)
print(numbers)

# 코드잇 후기ㅋㅋ
"""
정말 여러가지 방법으로 프로그래밍 기초 공부를 했었는데요. 여러번 포기했었습니다. 그러던 와중에 코드잇을 발견했고, 강의를 들어본 결과 코드잇이 단연코 최고입니다. 최고의 강사님과 최고의 강의를 제공해주신 코드잇에게 감사를 표합니다.

수많은 프로그래밍 강의가 있지만, 동영상 강의의 특성상, 멍하니 보고 머리로만 이해하고 넘어가게 되는 경우가 많습니다. 코드잇은 직접 자신의 손으로 코딩을 해보고, 퀘스트를 수행하듯이 진행되는 커리큘럼으로 강의듣고 고민해서 문제를 해결하고, 피드백 받고 하는 과정에서 머리로 이해하고 가슴으로 체화하게 됩니다. 손은 그것을 기억하고요.

이렇게 저렴한 가격으로, 하나하나 과외 선생님처럼 피드백까지 해주시니, 가히 대한민국 최고의 강의, 회사라고 불러도 될 것 같습니다.

저는 여러번 프로그래밍을 포기한 경험이 있었는데요. 최근 정보처리기사 자격증을 취득하고 보니, 알고리즘적 사고가 참 중요하다는 생각을 느꼈습니다. 예전에 잘 이해가 가지 않았던 것들이, 알고리즘 순서도 생각을 해보니 이해가 가기도 하는 것 같아요. 마침 코드잇 강의중에 알고리즘 강의도 있어서 들어볼 생각입니다.

대한민국에 많은 이들이 프로그래밍 교육을 외치고, 또 그것으로 돈벌이 사업을 하고 있는 와중에, 코드잇은 묵묵하게 정말 좋은 강의와, 프로그래밍 교육 서비스를 제공해주시는 것 같아서, 개인적으로 너무나 만족스럽고 또 감사하다는 말씀을 드리고 싶습니다.

아무쪼록 명실상부 대한민국 최고의 프로그래밍 교육 회사로 거듭나시길 기원하옵고, 온오프라인 프로그래밍 교육 서비스, 개발자 구인 구직, 개발자 커뮤니티, 나아가 대한민국 4차 산업혁명 시대를 앞당길 선구자적인 회사로의 발전을 기대하고 또 그렇게 될 줄로 믿습니다.

저도 정말 열심히 공부해서, 코드잇 대표님들 뵙고, 진로 상담을 하고, 개발자로서의 첫 발걸음을 코드잇과 함께 하고 싶은 소망도 있네요.

다시한번 감사하다는 말씀 드립니다. 감사합니다!
"""

# 리스트 꿀팁
"""
리스트에서 값의 존재 확인하기
print(7 in primes)
거꾸로 값이 없는지 확인하려면 in 앞에 not을 붙이면 됩니다.
print(7 not in primes)

리스트 안의 리스트 (Nested List)
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

sort 메소드
some_list.sort()는 새로운 리스트를 생성하지 않고 some_list를 정렬된 상태로 바꿔줍니다.
numbers.sort()

reverse 메소드
some_list.reverse()는 some_list의 원소들을 뒤집어진 순서로 배치합니다.
numbers.reverse()

index 메소드
some_list.index(x)는some_list에서 x의 값을 갖고 있는 원소의 인덱스를 리턴해줍니다.
print(members.index("윤수"))

remove 메소드
some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.
fruits.remove("파인애플")
"""
print()

# # 숫자 야구
#
# from random import randint
#
# numbers = []
#
# # 세개 뽑을때까지 반복
# while len(numbers) < 3:
#     new_number = randint(0, 9)
#
#     # 새로운 수 나올때까지 다시 뽑기
#     while new_number in numbers:
#         new_number = randint(0, 9)
#     numbers.append(new_number)
#
# print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
# print()
# print("세 수를 하나씩 차례대로 입력하세요.")
#
# # # 초기화
# # guesses = []
# # i = 0
# # strike = 0
# # ball = 0
# # tries = 0
#
# # 초기화
# strike = 0
# tries = 0
#
# # 전체 조건문 안에 넣기
# while strike < 3:
#
#     # 다시 초기화
#     guesses = []
#     i = 0
#     strike = 0
#     ball = 0
#     # tries = 0
#
#     # 1) 입력 2) 중복 메시지 3) 0 ~ 9 범위 경고 메시지
#     while len(guesses) < 3:
#         a = int(input("{}번째 수를 입력하세요: ".format(len(guesses) + 1)))
#
#         while a in guesses:
#             print("중복되는 수 입니다. 다시 입력해주세요.")
#             a = int(input("{}번째 수를 입력하세요: ".format(len(guesses) + 1)))
#
#         while a < 0 or 9 < a:
#             print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
#             a = int(input("{}번째 수를 입력하세요: ".format(len(guesses) + 1)))
#
#         guesses.append(a)
#
#     # 스트라이크랑 볼 세기
#     while i < 3:
#         if guesses[i] == numbers[i]:
#             strike += 1
#         elif guesses[i] in numbers:
#             ball += 1
#         i += 1
#
#     # 출력해주기
#     print(strike, "S", ball, "B")
#     tries += 1
#
# # 다 맞추면
# print("축하합니다. {}번만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(tries))

# 와따 어려웠다.
# 해설 잘 듣고
# 오늘 리스트 끝, 숫자야구 어려웠다. 근데 알고리즘적 사고를 하면 해결할 수는 있었다
# 무슨 말이냐면 변수설정하고 while반복문 잘 만들고 그 안에 또 while 문 만들고
# 어느 위치에서 초기화를 해줄 것인지 고민하고 등 문법만 숙지하면 나머지는 알고리즘 논리인 듯
# 계층과 층위랄까 여튼 문법 숙지 완벽하게 하고 논리적으로 문제해결하는 공부를 하면 될 것 같다.

# 정리하면 문법은 기본, 자유자재로 쓸 수 있도록 숙지해야 하고
# 이후는 변수설정, 반복문 사용 등, 알고리즘적 사고, 논리적으로 코딩짜야 되는 것 같다.
# 혼자 문제 풀려는 노력해보고 논리적으로 생각해보고
# 계속해서 문제를 풀어내려는 코딩 근육을 길러야겠다.

"""
피드백
1. a, i 와 같은 변수명은 아쉽습니다. 다른 언어긴 하지만,
링크와 같이 변수명 하나를 짓기 위해 이렇게 고려해야할 사항이 많습니다.
직업적으로 하는게 아닐지라도, 최소한 의미가 있는 단어로는 써주시는 것을 권장합니다^^
2. input은 43번째 줄로 충분하지 않을까요? 조건 판단을 while로만 하는 것은 아닐 것입니다.
"""

# 숫자 야구(수정)

from random import randint

numbers = []

# 세개 뽑을때까지 반복
while len(numbers) < 3:
    new_number = randint(0, 9)

    # 새로운 수 나올때까지 다시 뽑기
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print()
print("세 수를 하나씩 차례대로 입력하세요.")

# 초기화
strike = 0
tries = 0

# 전체 조건문 안에 넣기
while strike < 3:

    # 다시 초기화
    guesses = []
    strike_and_ball = 0
    strike = 0
    ball = 0
    # tries = 0

    # 1) 입력 2) 중복 메시지 3) 0 ~ 9 범위 경고 메시지
    while len(guesses) < 3:
        guess = int(input("{}번째 수를 입력하세요: ".format(len(guesses) + 1)))

        if guess in guesses:
            print("중복되는 수 입니다. 다시 입력해주세요.")

        if guess < 0 or 9 < guess:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")

        guesses.append(guess)

    # 스트라이크랑 볼 세기
    while strike_and_ball < 3:
        if guesses[strike_and_ball] == numbers[strike_and_ball]:
            strike += 1
        elif guesses[strike_and_ball] in numbers:
            ball += 1
        strike_and_ball += 1

    # 출력해주기
    print(strike, "S", ball, "B")
    tries += 1

# 다 맞추면
print("축하합니다. {}번만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(tries))
