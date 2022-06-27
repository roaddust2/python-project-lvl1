from brain_games.brain_engine import start_script
import prompt
import random
import time


# user's name
name = ''


# gcd check
def gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    return num_1 + num_2


# main function
def gcd_game():
    game_instruction = 'Find the greatest common divisor of given numbers.'
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        num_1 = random.randint(1, 99)
        num_2 = random.randint(1, 99)
        correct_answer = gcd(num_1, num_2)
        time.sleep(0.5)
        print(f'Question: {str(num_1)} {str(num_2)}')
        time.sleep(0.5)
        answer = prompt.string('Your answer: ')
        try:
            if int(answer) != correct_answer:
                time.sleep(0.5)
                return print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'
Let's try again, {name}!''')
            elif int(answer) == correct_answer and counter == 3:
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
