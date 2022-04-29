#!/usr/bin/env python

from sympy import isprime
import prompt
import random
from brain_games.scripts.brain_games import greet


def prime_number():

    name = greet()
    print("Answer \'yes\' if given number is prime. Otherwise answer \'no\'")
    counter = 3

    while counter > 0:

        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string("Your answer: ")
        fact = "yes" if isprime(number) else "no"

        is_correct = fact == answer

        if not is_correct:

            print(f'\'{answer}\' is wrong answer ;(.')
            print(f'Correct answer was \'{fact}\'')
            print(f'Let\'s try again, {name}!')
            return  # Just leave this game

        print("Correct!")
        counter -= 1

    print(f'Congratulations, {name}!')


def main():
    prime_number()


if __name__ == "__main__":
    main()
