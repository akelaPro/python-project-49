from random import randint


from brain_games.cli import welcome_user


def prime_num(num):
    count = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            break
    if count > 0:
        return('no')
    else:
        return('yes')

        
def prime_game():
    name = welcome_user()
    print('Answer "yes" if the number is зкшьу, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(2, 101)
        print(f'Question: {number}')
        n = input('yor answer: ')

        if  prime_num(number) == 'yes' and n.lower() == 'yes':
            print('Correct!')
            count += 1
        elif prime_num(number) == 'no' and n.lower() == 'no':
            print('Correct!')
            count += 1
        elif prime_num(number) == 'no' and n.lower() == 'yes':
            print(f"{n} is wrong answer ;(. Correct answer was 'no'.")
            print(f"let's try again,{name}")
        else:
            prime_num(number) == 'yes' and n.lower() == 'no'
            print(f"{n} is wrong answer ;(. Correct answer was 'yes'.")
            print(f"let's try again,{name}")
    if count == 3: 
        print (f'congratulations, {name}')

if __name__ == '__main__':
    prime_game()