from dataclasses import dataclass
from time import time
from abc import ABC, abstractmethod


class InvalidStateException(Exception):
    pass


class Game:
    def __init__(self, inp, problem_bank, num_tries) -> None:
        self.input: GameInput = inp
        self.problem_bank = problem_bank
        self.score = 0
        self.num_tries = num_tries

    def play(self):
        print(f"Number of tries: {self.num_tries}")
        problem: Problem
        for problem in self.problem_bank:
            print(f"Score: {self.score}")
            print(problem.problem)
            for _ in range(self.num_tries):
                guess = self.input.make_guess()
                if guess == problem.answer:
                    print("Correct Answer!")
                    self.score += 1
                    break
        print(f"Final Score: {self.score}")

    # def next_problem(self):
    #     try:
    #         self.problem = next(self.problem_bank)
    #     except StopIteration:
    #         self.problem = None


class GameInput(ABC):
    @abstractmethod
    def make_guess(self):
        pass


class PlayerInput(GameInput):
    def make_guess(self):
        inp = input("> ")
        try:
            inp = int(inp)
        except TypeError:
            pass
        return inp


class ProblemBank:
    def __init__(self, problems) -> None:
        self.problems = problems

    def __iter__(self):
        return iter(self.problems)

    def __next__(self):
        return next(iter(self.problems))


@dataclass
class Problem:
    problem: str
    answer: int | str


if __name__ == "__main__":
    # p = ProblemBank([1, 2, 3])
    # for prob in p:
    #     print(prob)

    # p = ProblemBank([1, 2, 3])
    # print(next(p))
    # print(next(p))
    # print(next(p))
    # for prob in p:
    #     print(prob)

    p1 = Problem("what is 5!", 120)
    problems = [p1]
    game = Game(PlayerInput(), [p1], 3)
    game.play()
