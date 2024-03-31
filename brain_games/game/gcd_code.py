from random import randint


from brain_games.cli import welcome_user


def gcd_code(num1, num2):
    divider1 = []
    divider2 = []
    result = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divider1.append(i)
    for j in range(1, num2 + 1):
        if num2 % j == 0:
            divider2.append(j)
    for k in divider1:
        if k in divider2:
            result.append(k)
    return max(result)


def gcd_game():
    name = welcome_user()
    print("Find the greatest common divisior of given numbers.")
    count = 0
    while count <3:
        num1 = randint(1, 101)
        num2 = randint(1, 101)
        print(f'Question: {num1} {num2}')
        n = int(input('Yor answer: '))
        if gcd_code(num1,num2) == n:
            print('Correct!')
            count += 1
        else:
            print(f"{n} is wrong answer ;(. Correct answer was {gcd_code(num1,num2)}.")
            print(f"let's try again,{name}")
            return
    if count == 3: 
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    gcd_game()