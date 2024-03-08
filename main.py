class Dog:
    def bark(self) -> None:
        print('гаф-гаф')


class Cat:
    def meow(self) -> None:
        pass


class Cow:
    def moo(self) -> None:
        pass


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
    pass


def sub(a: int, b: int) -> int:
    try:
        return a - b
    except:
        raise ValueError


def div(a: int, b: int) -> int:
    pass
