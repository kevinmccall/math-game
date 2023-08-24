from sys import exit
from problem import Problem
from game_input import GameInput


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
        for problem_num, problem in enumerate(self.problem_bank, start=1):
            print(f"Score: {self.score}")
            print(f"({problem_num}) {problem.prompt}")
            for _ in range(self.num_tries):
                guess = self.input.make_guess()
                if guess == problem.answer:
                    print("Correct answer!")
                    self.score += 1
                    break
            else:
                print(f"Wrong! The correct answer was {problem.answer}")
        print(f"Final Score: {self.score}")
