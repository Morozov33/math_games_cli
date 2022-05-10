"""Game tree: Find greatest common divisor of two number"""

from brain_games.greeting import welcome_user
from brain_games.task_of_game import task_of_game, win
from brain_games.initial_conditions import initial_conditions_gdc


def game_gcd():
    """Start game number three"""

    name_user = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count_true_answer = 0

    while count_true_answer < 3:
        (true_answer, number_1, number_2) = initial_conditions_gdc()
        print(f'Question: {number_1} {number_2}')
        count_true_answer = task_of_game(name_user, count_true_answer,
                                         true_answer)

    if count_true_answer == 3:
        return(win(name_user))
