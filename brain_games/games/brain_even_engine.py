from brain_games.brain_engine import start_script
import prompt
import random
import time


# user's name
name = ''


# is even check
def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


# main function
def even_game():
    game_instruction = 'Answer "yes" if the number is even, otherwise answer "no".'  # noqa: E501
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        question = random.randint(1, 99)
        time.sleep(0.5)
        print('Question: ' + str(question))
        time.sleep(0.5)
        answer = prompt.string('Your answer: ')
        if answer != is_even(question):
            time.sleep(0.5)
            return print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{is_even(question)}\'
Let's try again, {name}!''')
        elif answer == is_even(question) and counter == 3:
            time.sleep(0.5)
            print('Correct!')
            time.sleep(0.5)
            return print(f'Congratulations, {name}!')
        else:
            counter += 1
            time.sleep(0.5)
            print('Correct!')
    return
