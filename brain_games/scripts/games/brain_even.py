#!/usr/bin/env python

import prompt
import random
from brain_games.scripts.brain_games import greet


def is_even():

    correct = True
    number = 0
    name = greet()
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')

    while correct:

        number = random.randint(0, 100)
        even = number % 2 == 0
        not_even = number % 2 != 0
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if not_even and answer == 'yes' or even and answer == 'no':
            correct = False

    print(f"Let\'s try again, {name}!")


def main():
    is_even()


if __name__ == '__main__':
    main()
