"""Task of game"""

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
