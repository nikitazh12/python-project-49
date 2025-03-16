from brain_games.engine import run_game
from brain_games.games.calc import generate_question_and_answer, get_game_description

def main():
    run_game(get_game_description(), generate_question_and_answer)

if __name__ == '__main__':
    main()