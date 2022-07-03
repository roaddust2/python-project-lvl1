import random


RULE = 'What number is missing in the progression?'
PROGRESSION_LIMIT = 10


# Helper
#   Generating progression list
def generate_progression(num, diff):
    output = [num]
    counter = 1
    while counter <= PROGRESSION_LIMIT:
        output.append(num + diff)
        num += diff
        counter += 1
    return output


# Helper
#   Converting progression list to string for question
def convert_list_to_string(x_list, space):
    output = ''
    space = space
    for num in x_list:
        if num == x_list[space]:
            output += '..' + ' '
        else:
            output += str(num) + ' '
    return output


# Main function
def generate_question_and_answer():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    progression_full = generate_progression(num_1, num_2)
    space = random.randint(1, 10)
    question = convert_list_to_string(progression_full, space)
    correct_answer = str(progression_full[space])
    return question, correct_answer
