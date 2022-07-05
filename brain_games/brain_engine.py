import prompt


ROUNDS = 3

name = ''


def play(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)

    for _ in range(ROUNDS):
        question, correct_answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            msg = f"'{answer}' is wrong answer ;(." \
                  f"Correct answer was '{correct_answer}'.\n" \
                  f"Let's try again, {name}!"
            return print(msg)
        else:
            print('Correct!')

    print('Congratulations, {}!'.format(name))
