# Game number one for Brain Games

from brain_games.greeting import welcome_user
from brain_games.task_of_game import task_of_game


def game_1():
    """Start game number one"""

    name_user = welcome_user()
    print('Please, answer "yes" if the number is even, otherwise answer "no". '
          'You are ready?')
    count_true_answer = 0
    task_of_game(name_user, count_true_answer)
