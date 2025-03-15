import random
from brain_games.engine import run_game

def generate_question_and_answer():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer

def get_game_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'