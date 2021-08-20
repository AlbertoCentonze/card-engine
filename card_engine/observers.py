from abc import abstractmethod, ABC
from typing import TypeVar, Generic


class Observer(ABC):
    @abstractmethod
    def update(self, value):
        pass


class BooleanExpression(Observer):
    def __init__(self, condition):
        self.__condition = condition
        self.__value = False

    @property
    def value(self):
        return self.__value

    @value.getter
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        raise Exception("unsupported")

    def __repr__(self):
        return self.__value.__repr__()

    def update(self, value):
        new_value = self.__condition(value)
        if isinstance(new_value, bool):
            self.__value = new_value
        else:
            raise TypeError()

    def __bool__(self):
        return self.__value


BooleanExpression.register(bool)


class StringExpression(Observer, ABC):
    pass


T = TypeVar("T")


class Subject(Generic[T]):
    def __init__(self, value, observers=None):
        if observers is None:
            observers = []
        self.__observers: set = set()
        self.__value: T = value
        for o in observers:
            self.add_observer(o)

    def add_observer(self, observer):
        assert issubclass(type(observer), Observer) and observer not in self.__observers
        observer.update(self.value)
        self.__observers.add(observer)

    def remove_observer(self, observer):
        assert issubclass(type(observer), Observer) and observer in self.__observers
        observer.update(self.value())
        self.__observers.remove(observer)

    def __add__(self, other: Observer):
        self.add_observer(other)
        return self

    def __sub__(self, other: Observer):
        self.remove_observer(other)
        return self

    def __repr__(self):
        return f"obs: {self.__observers}"

    @property
    def value(self) -> T:
        return self.__value

    @value.setter
    def value(self, value: T) -> None:
        for o in self.__observers:
            o.update(value)
        self.__value = value

    @value.getter
    def value(self) -> T:
        return self.__value
