from sys import exit
from problem import Problem
from game_input import Input
from game_display import Display


class InvalidStateException(Exception):
    pass


class Game:
    def __init__(self, inp: Input, problem_bank, display: Display, num_tries) -> None:
        self.input = inp
        self.problem_bank = problem_bank
        self.score = 0
        self.num_tries = num_tries
        self.display = display

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
        self.display.display_message(f"Final Score: {self.score}")

    def incorrect_answer(self, problem):
        self.display.display_message(f"Wrong! The correct answer was {problem.answer}")

    def correct_answer(self):
        self.display.display_message("Correct answer!")

    def new_question_message(self, problem, problem_num):
        self.display.display_message(f"Score: {self.score}")
        self.display.display_message(f"({problem_num}) {problem.prompt}")

    def game_start_message(self):
        self.display.display_message(f"Number of tries: {self.num_tries}")
