# 남박사05-1
# 2019-12-01 09:51

# 클래스

class FishCakeMaker:
    def __init__(self, **kwargs):
        self._size = 10
        self._flavor = "팥"
        self._price = 100
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "flavor" in kwargs:
            self._flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self._price = kwargs.get("price")

    # def __del__(self):
    #     print("삭제 되었습니다.")

    def __lt__(self, other):
        return self._price < other._price

    def __le__(self, other):
        return self._price <= other._price

    def __gt__(self, other):
        return self._price > other._price
       
    def __ge__(self, other):
        return self._price >= other._price

    def __eq__(self, other):
         return self._price == other._price

    def __ne__(self, other):
         return self._price != other._price

    # __str__() 클래스가 print()에 의해 출력될 때 실행
    def __str__(self):
        return("<class FishCakeMake (size={}. price={}, flavor={})>".format(self._size, self._price, self._flavor))

    def show(self):
        print("붕어빵 종류 {}".format(self._flavor))
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 가격 {}".format(self._price))
        print("*" * 60)

# fish = FishCakeMaker("붕어빵")
# 생성해서 변수에 받았죠. 클래스가 생성이되는 순간 실행이 되는 순간 생성자라고 합니다.
# 클래스의 멤버함수와 변수에는 항상 self가 붙어야 합니다.

fish1 = FishCakeMaker()
fish2 = FishCakeMaker(size=20, price=300)
fish3 = FishCakeMaker(size=15, price=500, flavor="슈크림")

print(fish1)
print(fish2)
print(fish3)

print(fish1 > fish2)

# 상속
class MarketGoods(FishCakeMaker):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self._market_price = self._price + margin

    def show(self):
        print(self._flavor, self._market_price)

fish4 = MarketGoods(size=20, price=500)
fish4.show()