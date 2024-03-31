from random import randint


from brain_games.cli import welcome_user


from math import gcd


def gcd_code(item1, item2):
    return gcd(item1, item2)


def gcd_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    while count < 3:
        num1 = randint(1, 101)
        num2 = randint(1, 101)
        print(f'Question: {num1} {num2}')
        n = int(input('Yor answer: '))
        result = gcd_code(num1, num2)
        if gcd_code(num1, num2) == n:
            print('Correct!')
            count += 1
        else:
            print(f"{n} is wrong answer ;(. Correct answer was {result}.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    gcd_game()
