import random


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        correct_answer = str(num1 + num2)
    elif operation == '-':
        correct_answer = str(num1 - num2)
    elif operation == '*':
        correct_answer = str(num1 * num2)
    
    question = f'{num1} {operation} {num2}'
    return question, correct_answer


def get_game_description():
    return 'What is the result of the expression?'