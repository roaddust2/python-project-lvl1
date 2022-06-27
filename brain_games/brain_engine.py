import prompt
import time


def start_script(game_instruction):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    time.sleep(0.5)
    print('Hello, ' + name + '!')
    time.sleep(0.5)
    print(game_instruction)
    return name
