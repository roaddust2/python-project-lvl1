# Main engine of all games
import prompt


# Greeting
def start_script(game_instruction):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game_instruction)
    return name


# Cycle
#   the number of interations are defined in the game's engine
def cycle(name, question, correct_answer, counter):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer != correct_answer:
        counter = 4
        print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.
Let's try again, {name}!''')
        return counter
    elif answer == correct_answer and counter == 3:
        print('Correct!')
        print(f'Congratulations, {name}!')
        return counter
    else:
        print('Correct!')
        return counter
