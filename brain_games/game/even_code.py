from random import randint


from brain_games.cli import welcome_user


def even_numbers(num):
    return num % 2 == 0


def game_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(1, 101)
        print(f'Question: {number}')
        n = input('Yor answer: ')

        if even_numbers(number) and n.lower() == 'yes':
            print('Correct!')
            count += 1
        elif not even_numbers(number) and n.lower() == 'no':
            print('Correct!')
            count += 1
        elif not even_numbers(number) and n.lower() == 'yes':
            print(f"{n} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            even_numbers(number) and n.lower() == 'no'
            print(f"{n} is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
        

if __name__ == '__main__':
    game_even()
