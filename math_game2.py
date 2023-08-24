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
        self.game_start_message()
        problem: Problem
        for problem_num, problem in enumerate(self.problem_bank, start=1):
            self.new_question_message(problem, problem_num)
            for _ in range(self.num_tries):
                guess = self.input.make_guess()
                if guess == problem.answer:
                    self.correct_answer()
                    self.score += 1
                    break
            else:
                self.incorrect_answer(problem)
        self.game_completed_message()

    def game_completed_message(self):
        print(f"Final Score: {self.score}")

    def incorrect_answer(self, problem):
        print(f"Wrong! The correct answer was {problem.answer}")

    def correct_answer(self):
        print("Correct answer!")

    def new_question_message(self, problem, problem_num):
        print(f"Score: {self.score}")
        print(f"({problem_num}) {problem.prompt}")

    def game_start_message(self):
        print(f"Number of tries: {self.num_tries}")
