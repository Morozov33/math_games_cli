"""Task of game number one: even numbers.
User need three true answer for win this game."""


import random
import prompt


def task_of_game(name_user, count_true_answer):

    if count_true_answer != 3:
        number = random.randint(1, 100)
        true_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: number {number} is even?\n')
        user_answer = prompt.string('You answer: ')

        if user_answer == true_answer:
            print('Correct!')
            count_true_answer += 1
            task_of_game(name_user, count_true_answer)
        else:
            return(print(f'Oh, sorry, \"{user_answer}\" is not wrong answer :((\n'
                         f'Correct answer is \"{true_answer}\".\n'
                         f'Let\'s try again, {name_user}!'))
    else:
        return(print(f'Congratulations, {name_user}! You win!'))
