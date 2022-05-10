"""Calculete of initial conditions for four games"""

import random
import math


def initial_conditions_even():

    number = random.randint(1, 10)
    true_answer = 'yes' if number % 2 == 0 else 'no'

    return(true_answer, number)


def initial_conditions_calc():

    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    sign = random.choice('+-*')

    if sign == '+':
        true_answer = number_1 + number_2

    elif sign == '-':
        true_answer = number_1 - number_2

    elif sign == '*':
        true_answer = number_1 * number_2

    return(true_answer, number_1, number_2, sign)


def initial_conditions_gdc():

    number_1 = random.randint(1, 50)
    number_2 = random.randint(1, 50)
    true_answer = math.gcd(number_1, number_2)

    return(true_answer, number_1, number_2)


def initial_conditions_progression():

    start_prog = 1
    end_prog = 51
    step_prog = random.randint(5, 10)
    progression = list(range(start_prog, end_prog, step_prog))
    hidden_element = random.randint(0, len(progression) - 1)
    true_answer = progression[hidden_element]
    progression[hidden_element] = '...'
    progression = " , ".join(map(str, progression))
    return(true_answer, progression)


def initial_conditions_prime():

    number = random.randint(1, 30)
    true_answer = 'yes' if is_prime(number) is True else 'no'

    return(true_answer, number)


def is_prime(number):

    d = 2

    while d <= number / 2:

        if number % d != 0:
            d += 1

        else:
            return(False)

    return(True)
