import prompt
import time

def welcome_user():
    print("Welcome to the Brain Games!")

def start_script(game_name:str):
    name = prompt.string('May I have your name? ')
    time.sleep(0.5)
    print('Hello, ' + name + '!')
    if game_name == 'brain_even':
        time.sleep(0.5)
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_name == 'brain_calc':
        time.sleep(0.5)
        print('What is the result of the expression?')
    return name