from brain_games.brain_engine import start_script
from brain_games.brain_engine import cycle
import random


# User name
name = ''


# Helper
# Checking is number prime (yes/no) in string output
def is_prime(num):
    num_counter = 2
    while num_counter < num:
        if num % num_counter == 0:
            return 'no'
        else:
            num_counter += 1
    return 'yes'


# Main function
def prime_game():
    game_instruction = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        question = random.randint(3, 200)
        correct_answer = is_prime(question)
        counter = cycle(name, str(question), correct_answer, counter)
        counter += 1
    return
