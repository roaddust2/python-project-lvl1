import random


RULE = 'Find the greatest common divisor of given numbers.'


# Helper
#   Checking gcd of two numbers
def find_gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    return num_1 + num_2


# Main function
def generate_question_and_answer():
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    question = f'{num_1} {num_2}'
    correct_answer = find_gcd(num_1, num_2)
    return question, str(correct_answer)
