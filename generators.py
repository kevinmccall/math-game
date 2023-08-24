from random import choice, randint

from problem import Problem


class AdditionGenerator:
    def __init__(self, min_num, max_num) -> None:
        self.max_num = max_num
        self.min_num = min_num

    def __call__(self):
        a = randint(self.min_num, self.max_num)
        b = randint(self.min_num, self.max_num)
        prompt = f"{a} + {b} = ?"
        ans = a + b
        return Problem(prompt, ans)


class OperatorGenerator:
    def __init__(self, min_num, max_num, operation, symbol) -> None:
        self.max_num = max_num
        self.min_num = min_num
        self.operation = operation
        self.sybmol = symbol

    def __call__(self):
        a = randint(self.min_num, self.max_num)
        b = randint(self.min_num, self.max_num)
        prompt = f"{a} {self.sybmol} {b} = ?"
        ans = self.operation(a, b)
        return Problem(prompt, ans)


class ProblemFactory:
    def __init__(self, generators) -> None:
        self.generators = generators

    def __iter__(self):
        return self

    def __next__(self):
        generator = choice(self.generators)
        return generator()


def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def factorial_problem(n):
    prompt = f"What is {n}!"
    ans = factorial(n)
    return Problem(prompt, ans)
