from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display_message(self, message):
        pass


class ConsoleDisplay(Display):
    def display_message(self, message):
        print(message)
