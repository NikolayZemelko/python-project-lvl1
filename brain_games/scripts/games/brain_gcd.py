#!/usr/bin/env python

import random
import prompt
from brain_games.scripts.brain_games import greet


def what_is_gcd():

    name = greet()
    counter = 3

    print('Find the greatest common divisor of given numbers.')

    while counter > 0:

        first_num = random.randint(0, 200)
        second_num = random.randint(0, 200)
        min_num = min(first_num, second_num)
        common_max_div = 1
        divider = 1

        while divider <= min_num:
            if first_num % divider == 0 and second_num % divider == 0:
                common_max_div = divider
            divider += 1

        print(f'Question: {first_num} {second_num}')
        answer = prompt.string('Your answer: ')
        correct = str(common_max_div) == answer

        if correct:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(.')
            print(f'Correct answer \'{common_max_div}\'')
            print(f'Let`s try again, {name}')
            return  # EXIT is here, when you are wrong :(

        counter -= 1

    print(f'Congratulations, {name}!')


def main():
    what_is_gcd()


if __name__ == '__main__':
    main()
