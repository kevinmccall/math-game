from random import choice, randint
from time import time

from problem import Problem


class ProblemBank:
    def __init__(self, problems, iterator=None) -> None:
        if iterator is None:
            self.iter = iter(problems)
        else:
            self.iter = iterator
        self.problems = problems

    def __iter__(self):
        return self.iter

    def __next__(self):
        return next(self.iter)


class RandomBank:
    def __init__(self, problems) -> None:
        self.problems = list(problems)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.problems) == 0:
            raise StopIteration()
        question = choice(self.problems)
        self.problems.remove(question)
        return question


class TimedBank:
    def __init__(self, problems, time_to_guess) -> None:
        self.problems = problems
        self.time_to_guess = time_to_guess
        self.start_time = None
        self.iter = iter(problems)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_time is None:
            self.start_time = time()
        elif time() - self.start_time > self.time_to_guess:
            raise StopIteration()
        return next(self.iter)


class AdditionBank:
    def __init__(self, min_num, max_num, count) -> None:
        self.max_num = max_num
        self.min_num = min_num
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration()
        self.count -= 1
        a = randint(self.min_num, self.max_num)
        b = randint(self.min_num, self.max_num)
        prompt = f"{a} + {b} = ?"
        ans = a + b

        return Problem(prompt, ans)
