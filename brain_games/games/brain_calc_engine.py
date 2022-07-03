import random


RULE = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


# Helper
#   Calculator
def calculate(num_1, num_2, operator):
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    elif operator == '*':
        correct_answer = num_1 * num_2
    return correct_answer


# Main function
def generate_question_and_answer():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operator = random.choice(OPERATORS)
    question = f'{num_1} {operator} {num_2}'
    correct_answer = str(calculate(num_1, num_2, operator))
    return question, correct_answer
