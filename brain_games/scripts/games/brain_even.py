#!/usr/bin/env python

import prompt
import random
from brain_games.scripts.brain_games import greet


def is_even():

    correct = True
    number = 0
    name = greet()
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')

    counter = 3

    while counter > 0:

        number = random.randint(0, 100)
        even = number % 2 == 0
        fact = "yes" if even else "no"

        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        correct = answer == fact

        if not correct:

            print(f'\' {answer}\' is wrong answer ;(.')
            print(f'Correct answer was \'{fact}\'')
            print(f'Let\'s try again, {name}!')
            return  # Exit the game

        print("Correct!")
        counter -= 1

    print(f'Congratulations, {name}!')


def main():
    is_even()


if __name__ == '__main__':
    main()
