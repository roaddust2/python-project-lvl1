# Main engine of all games
import prompt
import time


# Greeting
def start_script(game_instruction):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    time.sleep(0.5)
    print('Hello, ' + name + '!')
    time.sleep(0.5)
    print(game_instruction)
    return name


# Cycle
#   the number of interations are defined in the game's engine
def cycle(name, question, correct_answer, counter):
    time.sleep(0.5)
    print(f'Question: {question}')
    time.sleep(0.5)
    answer = prompt.string('Your answer: ')
    if answer != correct_answer:
        counter = 4
        time.sleep(0.5)
        print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'
Let's try again, {name}!''')
        return counter
    elif answer == correct_answer and counter == 3:
        time.sleep(0.5)
        print('Correct!')
        time.sleep(0.5)
        print(f'Congratulations, {name}!')
        return counter
    else:
        time.sleep(0.5)
        print('Correct!')
        return counter
