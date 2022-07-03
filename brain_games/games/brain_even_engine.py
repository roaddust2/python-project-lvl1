import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


# Helper
#   Checking is numer even (yes/no) in string output
def check_is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


# Main function
def generate_question_and_answer():
    question = random.randint(1, 99)
    correct_answer = check_is_even(question)
    return question, correct_answer
