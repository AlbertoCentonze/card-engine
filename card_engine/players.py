from abc import abstractmethod, ABC
from random import choice


class Player(ABC):
    @abstractmethod
    def show_message(self, message: str) -> None:
        pass

    def show_question(self, message: str, options: list[str]) -> int:
        self.show_message(message)
        return self.choose(options)

    @abstractmethod
    def choose(self, options: list[str]) -> int:
        pass


class ConsolePlayer(Player):
    def show_message(self, message: str) -> None:
        print(message)

    def choose(self, options: list[str]) -> int:
        for index, option in enumerate(options):
            print(f"{index + 1} - {option}")
        return int(input()) - 1


class RandomPlayer(Player):
    def choose(self, options: list[str]) -> int:
        return choice(range(len(options)))

    def show_message(self, message: str) -> None:
        pass
