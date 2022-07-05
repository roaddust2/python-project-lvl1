import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    num_counter = 2
    while num_counter < num:
        if num % num_counter == 0:
            return False
        else:
            num_counter += 1
    return True


def generate_question_and_answer():
    question = random.randint(3, 200)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
