"""Greeting new user"""

import prompt


def welcome_user():
    """Greeting new user"""

    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name?\n')
    print(f'Hello, {name_user}!')
    return(name_user)
