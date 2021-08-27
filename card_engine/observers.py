from abc import abstractmethod, ABC
from typing import TypeVar, Generic


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


T = TypeVar("T")


class Subject(Generic[T], ABC):
    def __init__(self, value, observers: list[Observer] = None):
        if observers is None:
            observers = []
        self._observers: set = set()
        self._state: T = value
        for o in observers:
            self.attach(o)

    def attach(self, observer):
        assert issubclass(type(observer), Observer) and observer not in self._observers
        observer.update(self.state)
        self._observers.add(observer)

    def detach(self, observer):
        assert issubclass(type(observer), Observer) and observer in self._observers
        observer.update(self.state())
        self._observers.remove(observer)

    def notify(self):
        for o in self._observers:
            o.update(self._state)

    @property
    def state(self) -> T:
        return self._state

    @state.setter
    def state(self, new_state: T) -> None:
        update_necessary = self.set_state(new_state)
        if update_necessary:
            self.notify()

    @abstractmethod
    def set_state(self, value) -> bool:
        pass

    def __add__(self, other: Observer):
        self.attach(other)
        return self

    def __sub__(self, other: Observer):
        self.detach(other)
        return self

    def __repr__(self):
        return f"obs: {self._observers}"
