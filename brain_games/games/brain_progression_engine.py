from brain_games.brain_engine import start_script
import prompt
import random
import time


# user's name
name = ''


# progression helper
def progression(num, diff):
    output = [num]
    limit = 10
    counter = 1
    while counter < limit:
        output.append(num + diff)
        num += diff
        counter += 1
    return output


# progression_list to string helper
def progression_to_string(x_list, space):
    output = ''
    space = space
    for num in x_list:
        if num == x_list[space]:
            output += '..' + ' '
        else:
            output += str(num) + ' '
    return output


# main function
def progression_game():
    game_instruction = 'What number is missing in the progression?'
    name = start_script(game_instruction)
    counter = 1
    while counter <= 3:
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
        progression_full = progression(num_1, num_2)
        space = random.randint(0, 9)
        progression_string = progression_to_string(progression_full, space)
        correct_answer = progression_full[space]
        time.sleep(0.5)
        print(f'Question: {progression_string}')
        time.sleep(0.5)
        answer = prompt.string('Your answer: ')
        try:
            if int(answer) != progression_full[space]:
                time.sleep(0.5)
                return print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'
Let's try again, {name}!''')
            elif int(answer) == progression_full[space] and counter == 3:
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
