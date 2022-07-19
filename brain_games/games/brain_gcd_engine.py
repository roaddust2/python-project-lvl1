import random


RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(num_1, num_2):
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


def generate_question_and_answer():
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    question = f'{num_1} {num_2}'
    correct_answer = find_gcd(num_1, num_2)
    return question, str(correct_answer)
