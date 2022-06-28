from brain_games.brain_engine import start_script
from brain_games.brain_engine import cycle
import random


# User name
name = ''


# Helper
#   Checking gcd of two numbers
def gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    return num_1 + num_2


# Main function
def gcd_game():
    game_instruction = 'Find the greatest common divisor of given numbers.'
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        num_1 = random.randint(1, 99)
        num_2 = random.randint(1, 99)
        question = f'{str(num_1)} {str(num_2)}'
        correct_answer = str(gcd(num_1, num_2))
        counter = cycle(name, question, correct_answer, counter)
    return
