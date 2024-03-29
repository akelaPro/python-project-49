from random import randint, choice
<<<<<<< HEAD


from brain_games.cli import welcome_user


=======
from brain_games.cli import welcome_user
>>>>>>> 011fcd61951bfb5304d0300577077a42bd8e14d5
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
<<<<<<< HEAD
    while count < 3:
        num1 = randint(1, 101)
        num2 = randint(1, 101)
        operator = choice(['+', '-', '*'])
=======
    while count <3:
        num1 = randint(1,101)
        num2 = randint(1,101)
        operator = choice(['+','-','*'])
>>>>>>> 011fcd61951bfb5304d0300577077a42bd8e14d5
        print(f'Question: {num1} {operator} {num2}')
        n = int(input('yor answer: '))
        if calc_game(num1, num2, operator) == n:
            print('Correct!')
<<<<<<< HEAD
            count += 1
        else:
            print(f"{n} is wrong answer ;(. Correct answer was {calc_game(num1, num2, operator)}.")
            print(f"let's try again,{name}")
    if count == 3:
=======
            count +=1
        else:
            print(f"{n} is wrong answer ;(. Correct answer was {calc_game(num1, num2, operator)}.")
            print(f"let's try again,{name}")
    if count ==3:
>>>>>>> 011fcd61951bfb5304d0300577077a42bd8e14d5
        print(f'Congratulation, {name}!')


if __name__ == '__main__':
    calc()
