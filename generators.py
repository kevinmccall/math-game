from random import choice, randint

from time import time

from problem import Problem


class AdditionGenerator:
    def __init__(self, a_min, a_max, b_min, b_max) -> None:
        self.a_min = a_min
        self.a_max = a_max
        self.b_min = b_min
        self.b_max = b_max

    def __call__(self):
        a = randint(self.a_min, self.a_max)
        b = randint(self.b_min, self.b_max)
        prompt = f"{a} + {b} = ?"
        ans = a + b
        return Problem(prompt, ans)


class SubtractionGenerator:
    def __init__(self, a_min, a_max, b_min, b_max) -> None:
        self.a_min = a_min
        self.a_max = a_max
        self.b_min = b_min
        self.b_max = b_max

    def __call__(self):
        a = randint(self.a_min, self.a_max)
        b = randint(self.b_min, self.b_max)
        prompt = f"{a + b} - {a} = ?"
        return Problem(prompt, b)


class MultiplicationGenerator:
    def __init__(self, a_min, a_max, b_min, b_max) -> None:
        self.a_min = a_min
        self.a_max = a_max
        self.b_min = b_min
        self.b_max = b_max

    def __call__(self):
        a = randint(self.a_min, self.a_max)
        b = randint(self.b_min, self.b_max)
        prompt = f"{a} * {b} = ?"
        ans = a * b
        return Problem(prompt, ans)


class DivisionGenerator:
    def __init__(self, a_min, a_max, b_min, b_max) -> None:
        self.a_min = a_min
        self.a_max = a_max
        self.b_min = b_min
        self.b_max = b_max

    def __call__(self):
        a = randint(self.a_min, self.a_max)
        b = randint(self.b_min, self.b_max)
        product = a * b
        prompt = f"{product} / {a} = ?"
        return Problem(prompt, b)


class FactorialGenerator:
    def __init__(self, a_min, a_max) -> None:
        self.a_min = a_min
        self.a_max = a_max

    def __call__(self):
        a = randint(self.a_min, self.a_max)
        prompt = f"{a}! = ?"
        return Problem(prompt, factorial(a))


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


def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def factorial_problem(n):
    prompt = f"What is {n}!"
    ans = factorial(n)
    return Problem(prompt, ans)
