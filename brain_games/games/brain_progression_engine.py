from brain_games.brain_engine import start_script
from brain_games.brain_engine import cycle
import random


# User name
name = ''


# Helper
#   Generating progression list
def progression(num, diff):
    output = [num]
    limit = 10
    counter = 1
    while counter <= limit:
        output.append(num + diff)
        num += diff
        counter += 1
    return output


# Helper
#   Converting progression list to string for question
def progression_to_string(x_list, space):
    output = ''
    space = space
    for num in x_list:
        if num == x_list[space]:
            output += '..' + ' '
        else:
            output += str(num) + ' '
    return output


# Main function
def progression_game():
    game_instruction = 'What number is missing in the progression?'
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
        progression_full = progression(num_1, num_2)
        space = random.randint(1, 10)
        question = progression_to_string(progression_full, space)
        correct_answer = str(progression_full[space])
        counter = cycle(name, question, correct_answer, counter)
        counter += 1
    return
