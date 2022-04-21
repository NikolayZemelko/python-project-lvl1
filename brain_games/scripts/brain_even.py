#!/usr/bin/env python

import prompt
import random
from brain_games.scripts.brain_games import greet


def is_even():

    correct = True
    number = 0
    greet()
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')

    while correct:
        
        number = random.randint(0, 100)
        even = True if number % 2 == 0 else False
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        correct = True if even == True and answer == 'yes' or even == False and answer == 'no' else False

    print("Let\'s try again, Bill!")


def main():
    is_even()


if __name__ == '__main__':
    main()
