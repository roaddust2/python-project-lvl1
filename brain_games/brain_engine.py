# Main engine of all games
import prompt


# Number of rounds
ROUNDS = 3

# Player's name variable
name = ''


# Main function
def play(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    counter = 1

    while counter <= ROUNDS:
        question, correct_answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            return print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.
Let's try again, {name}!''')
        elif answer == correct_answer and counter == 3:
            return print(f'''Correct!
Congratulations, {name}!''')
        else:
            print('Correct!')
            counter += 1
    return
