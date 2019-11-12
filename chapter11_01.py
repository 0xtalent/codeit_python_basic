# Chapter11-1
# 객체 지향 프로그래밍

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# class 기초 정리

"""
페이스북같은 SNS를 만들려면 '유저'는 어떻게 표현해야 할까요?
'유저'는 이름, 이메일, 비밀번호, 생년월일, 친구목록 등 구성이 굉장히 복잡합니다.
문자열 하나로도 표현할 수 없고, 리스트로도 표현할 수 없습니다.

기존의 자료형들로 표현하기 어려운 것들은 우리가 새로운 자료형을 만들어서 표현할 수 있습니다.
SNS를 위해서는 '유저'라는 새로운 자료형을 만들면 되겠죠?

파이썬에서 새로운 자료형을 만들려면 '클래스'라는 것을 써야합니다.
클래스는 어떤 자료형에 대한 설명서라고 생각할 수 있습니다.

클래스 정의

class User:
    pass

# User값들 생성
user1 = User()
user2 = User()

<class '__main__.User'>라고 나와있는 것을 확인할 수 있습니다.
1이 int 클래스의 값이고 "hello"는 str 클래스의 값입니다.

인스턴스

class User:
    pass

user1 = User()
user2 = User()

print(user1 == user2)

User()를 호출하면 메모리의 특정 공간에 새로운 User 값이 생성되고,
그 메모리 주소가 리턴돼서 user1과 user2에 저장됩니다.
그런데 User()를 호출할때마다 새로운 메모리 공간에 값을 생성하기 때문에
user1과 user2는 엄밀히 따지면 다른 값, 또는 다른 인스턴스입니다.
따라서 user1 == user2는 False가 나오는 것입니다!
"""

# 인스턴스 변수, 메소드 정리

"""
인스턴스 변수
각 인스턴스는 여러가지 인스턴스 변수를 보관할 수 있습니다.

메소드

클래스는 변수뿐만 아니라 함수도 보관할 수 있습니다.
클래스에 정의된 함수는 메소드라고 부릅니다.
"""

# initialize 문제

class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)

"""
여기서 user1.initialize("Young", "young@codeit.kr", "123456")을 호출하면
User 클래스의 initialize 메소드가 실행되고 첫번째 파라미터로 인스턴스 user1이
넘어가게 됩니다. 그리고 "Young", "young@codeit.kr", "123456" 이 순서대로
2~4번째 파라미터로 넘어가게 됩니다.

따라서 아래 두 줄은 같다고 볼 수 있습니다:

user1.initialize("Young", "young@codeit.kr", "123456")
User.initialize(user1, "Young", "young@codeit.kr", "123456")

이렇게 쓰면 user1이 self로 넘어가고, "Young"이 name으로 넘어갑니다.
따라서 self.name = name은 user1.name = "Young"과 같은거죠.
"""

# __init__ 정리

"""
정의되어 있지 않은 인스턴스 변수를 사용하면 오류가 나오기 때문에
꼭 모든 인스턴스 변수를 정의해야 합니다.

그런데 보시다시피 매번 User 인스턴스를 생성하는 줄을 하나 쓰고, 초기값을 설정해주기 위해서
initialize 메소드를 호출하는 줄을 하나 썼습니다. 뭔가 좀 번거롭죠?

다행히 파이썬은 인스턴스 생성과 초기값 설정을 한번에 해결할 수 있도록
__init__이라는 특별한 메소드를 쓸 수 있게 해줍니다.

__init__ 메소드를 정의해놓으면 이제 유저 생성과 초기값 설정을 이렇게 깔끔하게 할 수 있습니다:

1. 메모리가 할당되고 User 인스턴스가 생성됩니다.
2. __init__ 메소드가 호출됩니다. 파라미터 self로는 생성된 인스턴스가 넘어가고 name, email, password로는 "Young", "young@codeit.kr", "123456"이 각각 넘어갑니다. 이 경우 인스턴스 변수들의 초기값이 모두 설정되는 거죠.
3. 만들어진 User 인스턴스가 리턴돼서 변수 user1에 저장됩니다.
"""

# 자기소개 문제

# sns의 유저
class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 자기 소개 (이름, 이메일)
    def introduce(self):
        print("My name is {}".format(self.name))
        print("My email address is {}".format(self.email))

    # 자기 소개 두번
    def introduce_twice(self):
        self.introduce()
        self.introduce()

# 테스트
user1 = User("Young", "young@codeit.kr", "123456")
user1.introduce()
user1.introduce_twice()

# 맞팔해요 문제

class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)

    # 몇명을 팔로우하는지 리턴
    def num_following(self):
        return len(self.following_list)

    # 팔로워가 몇명인지 리턴
    def num_followers(self):
        return len(self.followers_list)

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 테스트
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())
