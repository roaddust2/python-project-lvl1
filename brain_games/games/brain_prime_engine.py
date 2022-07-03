import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Helper
# Checking is number prime (yes/no) in string output
def check_is_prime(num):
    num_counter = 2
    while num_counter < num:
        if num % num_counter == 0:
            return 'no'
        else:
            num_counter += 1
    return 'yes'


# Main function
def generate_question_and_answer():
    question = random.randint(3, 200)
    correct_answer = check_is_prime(question)
    return question, correct_answer
