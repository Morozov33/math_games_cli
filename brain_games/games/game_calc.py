"""Game number two: calculate two numbers.
User need three true answer for win this game."""

from brain_games.greeting import welcome_user
from brain_games.task_of_game import task_of_game, initial_conditions, win


def game_calc():
    """Start game number two: calculate two number"""

    name_game = 'calc'
    name_user = welcome_user()
    print('What is the result of the expression?')
    count_true_answer = 0

    while count_true_answer < 3:
        (true_answer, number_1, number_2, sign) = initial_conditions(name_game)
        print(f'Question: {number_1} {sign} {number_2} = ?')
        count_true_answer = task_of_game(name_user, count_true_answer,
                                         true_answer)

    if count_true_answer == 3:
        return(win(name_user))
