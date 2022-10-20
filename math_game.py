from random import randint
import time

DEFAULT_MIN = 0
DEFAULT_MAX = 100
DEFAULT_TIME_SECONDS = 30

class Problem:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.operator = "!!!"

    def answer(self, guess):
        return guess == self._get_result() and guess is not None

    def _get_result(self):
        return None

    def get_problem(self):
        return f"{self.a} {self.operator} {self.b} = ?"

class AdditionProblem(Problem):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.operator = "+"

    def _get_result(self):
        return self.a + self.b

class SubtractionProblem(Problem):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.operator = "-"

    def _get_result(self):
        return self.a - self.b

class MultiplicationProblem(Problem):
    def __init__(self, a, b):
        super().__init__(a,b)
        self.operator = "*"

    def _get_result(self):
        return self.a * self.b

class DivisionProblem(Problem):
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError()
        if a % b != 0:
            raise ValueError("a needs to be a multiple of b")
        super().__init__(a, b)
        self.operator = "/"

    def _get_result(self):
        return self.a // self.b

def generate_problem(low, high):
    problem_type = randint(0,3)
    problem = None
    match problem_type:
        case 0:
            a = randint(low, high)
            b = randint(low, high)
            problem = AdditionProblem(a,b)
        case 1:
            a = randint(low, high)
            b = randint(low, high)
            problem = SubtractionProblem(a,b)
        case 2:
            a = randint(low, high)
            b = randint(low, high)
            problem = MultiplicationProblem(a,b)
        case 3:
            b = randint(low, high)
            while b == 0:
                b = randint(low, high)
            a = b * randint(low, high)
            problem = DivisionProblem(a, b)
    return problem

def main():
    playing = True
    score = 0
    start_time = time.time()
    while playing:
        problem = generate_problem(DEFAULT_MIN, DEFAULT_MAX)
        print(problem.get_problem(), f"{round(DEFAULT_TIME_SECONDS - (time.time() - start_time), 1)} seconds remaining")
        tries = 1
        correct = False
        try:
            while playing and not correct and tries >= 0: 
                response = input("-> ")
                if response.lower() in ["q", "quit", "exit", "stop"]:
                    print("bye bye")
                    playing = False
                    continue
                elif response.lower() in ["skip", "s", "next", "n"]:
                    correct = False
                    continue
                elif response == ":(":
                    print(":c")
                    continue
                try:
                    response = int(response)
                except ValueError:
                    print("please enter a solution or quit")
                    continue
                if problem.answer(response):
                    score += 1
                    correct = True
                    print("Correct!")
                else:
                    if tries > 1:
                        print(f"Incorrect, {tries} tries remaining")
                    elif tries == 1:
                        print(f"Incorrect, {tries} try remaining")
                    else:
                        print(f"The answer was {problem._get_result()}")
                    tries -= 1
                
            if time.time() - start_time > DEFAULT_TIME_SECONDS:
                playing = False
                print("out of time!")
            
        except KeyboardInterrupt:
            print()
            print("bye byeeeee")
            playing = False
    print(f"score: {score}")

if __name__ == '__main__':
    main()
