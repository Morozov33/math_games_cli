"""Game number one: even numbers.
User need three true answer for win this game."""

from brain_games.greeting import welcome_user
from brain_games.task_of_game import task_of_game, initial_conditions, win


def game_even():
    """Start game number one"""

    name_game = 'even'
    name_user = welcome_user()
    print('Please, answer "yes" if the number is even, otherwise answer "no". '
          'You are ready?')
    count_true_answer = 0

    while count_true_answer < 3:
        (true_answer, number) = initial_conditions(name_game)
        print(f'Question: {number} is even number?')
        count_true_answer = task_of_game(name_user, count_true_answer,
                                         true_answer)

    if count_true_answer == 3:
        return(win(name_user))
