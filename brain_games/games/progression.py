import random


def generate_question_and_answer():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 15)
    hidden_index = random.choice(0, length - 1)
    
    progression = [str(start + step * i) for i in range(length)]
    
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    
    return question, correct_answer


def get_game_description():
    return 'What number is missing in the progression?'