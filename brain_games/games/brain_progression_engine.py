import random


RULE = 'What number is missing in the progression?'
PROGRESSION_LIMIT = 10


def generate_progression(num, diff):
    output = [str(num)]
    counter = 1
    while counter <= PROGRESSION_LIMIT:
        output.append(str(num + diff))
        num += diff
        counter += 1
    return output


def convert_list_to_string(prog_list, space):
    new_prog_list = []
    new_prog_list[:] = prog_list
    new_prog_list[space] = '..'
    return ' '.join(new_prog_list)


def generate_question_and_answer():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    prog_list = generate_progression(num_1, num_2)
    space = random.randint(1, 10)
    question = convert_list_to_string(prog_list, space)
    correct_answer = prog_list[space]
    return question, correct_answer
