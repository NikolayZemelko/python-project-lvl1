#!/usr/bin/env python

from brain_games.cli import welcome_user


def greet():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    return name


def main():
    greet()


if __name__ == "__main__":
    main()
