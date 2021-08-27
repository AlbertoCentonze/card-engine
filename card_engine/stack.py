import random


class Stack:
    def __init__(self, initial: list = None, draw: bool = True, add: bool = False, peek: int = 1, shuffle: bool = False):
        self._stack = list(initial)
        if shuffle:
            self.shuffle()

    def shuffle(self) -> Stack:
        random.shuffle(self._stack)
        return self
