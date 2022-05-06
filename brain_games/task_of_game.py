"""Task of game"""

import random
import prompt


def task_of_game(name_user, count_true_answer, true_answer):

    user_answer = int(prompt.string('You answer: '))
    if user_answer == true_answer:
        print('Correct!')
        count_true_answer += 1
        return count_true_answer

    elif user_answer != true_answer:
        print(f'Oh, sorry, \"{user_answer}\" is not wrong answer :((\n'
              f'Correct answer is \"{true_answer}\".\n'
              f'Let\'s try again, {name_user}!')
        count_true_answer = 4
        return count_true_answer


def win(name_user):

    return(print(f'Congratulations, {name_user}! You win!'))


def initial_conditions(name_of_game):

    if name_of_game == 'even':
        number = random.randint(1, 10)
        true_answer = 'yes' if number % 2 == 0 else 'no'
        return(true_answer, number)

    elif name_of_game == 'calc':
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
