from abc import ABC, abstractmethod


class GameInput(ABC):
    @abstractmethod
    def make_guess(self):
        pass


class PlayerInput(GameInput):
    def make_guess(self):
        inp = input("> ")
        try:
            inp = int(inp)
        except ValueError:
            pass
        return inp
