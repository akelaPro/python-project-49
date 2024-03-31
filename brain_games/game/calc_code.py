from random import randint, choice


from brain_games.cli import welcome_user


def calc_game(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def calc():
    name = welcome_user()
    print("What is the result of the expression?")
    count = 0

    while count < 3:
        num1 = randint(1, 101)
        num2 = randint(1, 101)
        operator = choice(['+', '-', '*'])
        num1 = randint(1,101)
        num2 = randint(1,101)
        operator = choice(['+','-','*'])
        print(f'Question: {num1} {operator} {num2}')
        n = int(input('yor answer: '))
        if calc_game(num1, num2, operator) == n:
            print('Correct!')
            count += 1
        else:
            print(f"{n} is wrong answer ;(. Correct answer was {calc_game(num1, num2, operator)}.")
            print(f"let's try again,{name}")
            break
        if count == 3:
            print(f'Congratulation, {name}!')


if __name__ == '__main__':
    calc()
