from brain_games.brain_engine import start_script
from brain_games.brain_engine import cycle
import random


# User name
name = ''


# Helper
#   Checking is numer even (yes/no) in string output
def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


# Main function
def even_game():
    game_instruction = 'Answer "yes" if the number is even, otherwise answer "no".'  # noqa: E501
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        num = random.randint(1, 99)
        question = str(num)
        correct_answer = is_even(num)
        counter = cycle(name, question, correct_answer, counter)
        counter += 1
    return
