"""Game four: Find member of progression"""

from brain_games.greeting import welcome_user
from brain_games.task_of_game import task_of_game, win
from brain_games.initial_conditions import initial_conditions_progression


def game_progression():
    """Start game number four"""

    name_user = welcome_user()
    print('What number is missing in the progression?')
    count_true_answer = 0

    while count_true_answer < 3:
        (true_answer, progression) = initial_conditions_progression()
        print(f'Question: {progression}')
        count_true_answer = task_of_game(name_user, count_true_answer,
                                         true_answer)

    if count_true_answer == 3:
        return(win(name_user))
