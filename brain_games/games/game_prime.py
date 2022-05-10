"""Game number five: determine if a number is prime.
User need three true answer for win this game."""

from brain_games.greeting import welcome_user
from brain_games.task_of_game import task_of_game, win
from brain_games.initial_conditions import initial_conditions_prime


def game_prime():
    """Start game number five: djetermine if a number is prime"""

    name_user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_true_answer = 0

    while count_true_answer < 3:
        (true_answer, number) = initial_conditions_prime()
        print(f'Question: {number} is prime?')
        count_true_answer = task_of_game(name_user, count_true_answer,
                                         true_answer)

    if count_true_answer == 3:
        return(win(name_user))
