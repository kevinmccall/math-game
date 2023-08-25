from abc import ABC, abstractmethod


class Input(ABC):
    @abstractmethod
    def make_guess(self):
        pass


class PlayerInput(Input):
    def make_guess(self):
        inp = input("> ")
        try:
            inp = int(inp)
        except ValueError:
            pass
        return inp
