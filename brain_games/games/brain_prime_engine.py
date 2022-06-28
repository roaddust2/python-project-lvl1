from brain_games.brain_engine import start_script
import prompt
import random
import time


# user's name
name = ''


# is_prime helper
def is_prime(num):
    num_counter = 2
    while num_counter < num:
        if num % num_counter == 0:
            return 'no'
        else:
            num_counter += 1
    return 'yes'


# main function
def prime_game():
    game_instruction = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        question = random.randint(3, 200)
        correct_answer = is_prime(question)
        time.sleep(0.5)
        print(f'Question: {str(question)}')
        time.sleep(0.5)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            time.sleep(0.5)
            return print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'
Let's try again, {name}!''')
        elif answer == correct_answer and counter == 3:
            time.sleep(0.5)
            print('Correct!')
            time.sleep(0.5)
            return print(f'Congratulations, {name}!')
        else:
            counter += 1
            time.sleep(0.5)
            print('Correct!')
    return
