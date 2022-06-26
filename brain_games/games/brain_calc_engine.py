from brain_games.brain_engine import welcome_user
from brain_games.brain_engine import start_script
import prompt
import random
import time


# user's name
name = ''


# operator helper
def calc(num_1, num_2, operator):
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    elif operator == '*':
        correct_answer = num_1 * num_2
    return correct_answer


# main function
def calc_game():
    welcome_user()
    name= start_script('brain_calc')
    counter = 1
    while counter <= 3:
        num_1 = random.randint(1, 99)
        num_2 = random.randint(1, 99)
        operator_list = ['+', '-', '*']
        operator = random.choice(operator_list)
        correct_answer = calc(num_1, num_2, operator)
        time.sleep(0.5)
        print(f'Question: {str(num_1)} {operator} {str(num_2)}')
        time.sleep(0.5)
        answer = prompt.string('Your answer: ')
        try:
            if int(answer) != correct_answer:
                time.sleep(0.5)
                return print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'
Let's try again, {name}!''')
            elif int(answer) == calc(num_1, num_2, operator) and counter == 3:
                time.sleep(0.5)
                print('Correct!')
                time.sleep(0.5)
                return print(f'Congratulations, {name}!')
            else:
                counter += 1
                time.sleep(0.5)
                print('Correct!')
        except ValueError:
            time.sleep(0.5)
            return print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'
Let's try again, {name}!''')
    return
