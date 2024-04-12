import prompt


from brain_games.cli import welcome_user


def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    count = 0

    while count < 3:
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break

        print(f'Congratulations, {name}!')
