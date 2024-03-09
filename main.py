class Dog:
    def bark(self) -> None:
        print('гаф-гаф')


class Cat:
    def meow(self) -> None:
        pass


class Cow:
    def moo(self) -> None:
        print('му-му')


class Car:
    def __init__(self, mark: str):
        pass

    def drive(self) -> None:
        pass


class Engine(Car):
    def repair(self) -> None:
        pass


def get_user_data(row_num: int) -> str:
    pass


def summ(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def sub(a: int, b: int) -> int:
    try:
        return a - b
    except:
        raise ValueError


def div(a: int, b: int) -> int:
    return a/b

dog = Dog()
dog.bark()

cat = Cat()
cat.meow()

cow = Cow()
cow.moo()

honda = Car('sedan')
print(honda.drive())

v8 = Engine('honda')
print(v8.repair())

print(get_user_data(1))

print(summ(5, 10))

print(mul(5, 10))

print(sub(10, 5))

print(div(10, 5))