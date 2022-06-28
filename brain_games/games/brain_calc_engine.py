from brain_games.brain_engine import start_script
from brain_games.brain_engine import cycle
import random


# User name
name = ''


# Helper
#   Calculator
def calc(num_1, num_2, operator):
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    elif operator == '*':
        correct_answer = num_1 * num_2
    return correct_answer


# Main function
def calc_game():
    game_instruction = 'What is the result of the expression?'
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        num_1 = random.randint(1, 99)
        num_2 = random.randint(1, 99)
        operator_list = ['+', '-', '*']
        operator = random.choice(operator_list)
        question = f'{str(num_1)} {operator} {str(num_2)}'
        correct_answer = str(calc(num_1, num_2, operator))
        counter = cycle(name, question, correct_answer, counter)
        counter += 1
    return
