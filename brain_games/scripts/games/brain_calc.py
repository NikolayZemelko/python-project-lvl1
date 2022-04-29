#!/usr/bin/env python

from brain_games.scripts.brain_games import greet
import random
import prompt


def calc():

    name = greet()
    print('What is the result of the expression?')
    is_correct = True
    action_list = '-+*'
    action_left = len(action_list) - 1

    while is_correct and action_left >= 0:

        first_num = random.randint(0, 100)
        second_num = random.randint(0, 100)
        action_ind = random.randint(0, action_left)
        action = action_list[action_ind]
        action_list = action_list.replace(action, '')
        action_left -= 1
        expression = f'{first_num} {action} {second_num}'
        correct_answer = eval(expression)
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        is_correct = answer == str(correct_answer)

        if is_correct:
            print('Correct!')
        else:
            print(f'\'{answer}\' is a wrong answer ;(.')
            print(f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')


def main():
    calc()


if __name__ == '__main__':
    main()
