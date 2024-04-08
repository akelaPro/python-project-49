import prompt


from brain_games.cli import welcome_user


ROUND_COUNT = 3


def run_game(game_module):
    user_name = welcome_user()
    print(game_module.DESCRIPTION)
    while ROUND_COUNT != 0:
        question, correct_answer = game_module.generate_round()
        print('Question:', question)
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            ROUND_COUNT -=1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")