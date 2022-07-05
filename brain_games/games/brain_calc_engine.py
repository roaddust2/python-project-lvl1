import random


RULE = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def calculate(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '-':
        return num_1 - num_2
    elif operator == '*':
        return num_1 * num_2


def generate_question_and_answer():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operator = random.choice(OPERATORS)
    question = f'{num_1} {operator} {num_2}'
    correct_answer = str(calculate(num_1, num_2, operator))
    return question, correct_answer
