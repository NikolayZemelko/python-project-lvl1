#!/usr/bin/env python


from brain_games.scripts.brain_games import greet
import prompt
import random


def arith_progression():

    name = greet()
    print('What number is missing in the progression?')
    questions = 3

    while questions > 0:

        pr_ssn_start = random.randint(0, 100)
        pr_ssn_len = random.randint(5, 10)
        pr_ssn_step = random.randint(2, 50)
        pr_ssn_hide = random.randint(0, pr_ssn_len - 1)
        pr_ssn = []
        counter = pr_ssn_len

        while counter > 0:

            pr_ssn.append(str(pr_ssn_start))
            pr_ssn_start = pr_ssn_start + pr_ssn_step
            counter -= 1

        hidden_num = pr_ssn[pr_ssn_hide]
        pr_ssn.pop(pr_ssn_hide)
        pr_ssn.insert(pr_ssn_hide, '..')

        conv_str = ' '.join(pr_ssn)
        print(f'Question: {conv_str}')
        answer = prompt.string('Your answer: ')

        if answer != str(hidden_num):
            print(f'\'{answer}\' is wrong answer ;(.')
            print(f'Correct answer was \'{hidden_num}\'')
            print(f'Let`s try again, {name}!')
            return

        questions -= 1
        print('Correct!')

    print(f'Congratulations, {name}!')


def main():
    arith_progression()


if __name__ == '__main__':
    main()
