import prompt  # type: ignore

from brain_games.cli import welcome_user


def run_game(game_description, generate_question_and_answer):
    user_name = welcome_user()
    print(game_description)
    
    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        question, correct_answer = generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.") # noqa
            print(f"Let's try again, {user_name}!")
            return
        
    print(f'Congratulations, {user_name}!')
    