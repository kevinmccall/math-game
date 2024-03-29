from math_game2 import Game

from problem_bank import TimedBank, CountProblemFactory, TimedProblemFactory

from generators import *

from game_input import PlayerInput

from game_display import ConsoleDisplay

from sys import exit


def main():
    # p = ProblemBank([1, 2, 3])
    # for prob in p:
    #     print(prob)

    # p = ProblemBank([1, 2, 3])
    # print(next(p))
    # print(next(p))
    # print(next(p))
    # for prob in p:
    #     print(prob)

    # problems = [
    #     factorial_problem(1),
    #     factorial_problem(2),
    #     factorial_problem(3),
    #     factorial_problem(4),
    #     factorial_problem(5),
    #     factorial_problem(6),
    #     factorial_problem(7),
    #     factorial_problem(8),
    #     factorial_problem(9),
    # ]
    generators = [
        AdditionGenerator(2, 100, 2, 100),
        SubtractionGenerator(2, 100, 2, 100),
        MultiplicationGenerator(2, 12, 2, 100),
        DivisionGenerator(2, 12, 2, 100),
    ]
    # bank = ProblemBank(problems)
    # bank = RandomBank(problems)
    # bank = TimedBank(problems, 10)
    # bank = CountProblemFactory(generators, 5)
    bank = TimedProblemFactory(generators, 10)
    display = ConsoleDisplay()
    game = Game(PlayerInput(), bank, display, 3)
    game.play()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as k:
        print("bye bye!!!")
        exit()
