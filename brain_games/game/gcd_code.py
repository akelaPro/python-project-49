<<<<<<< HEAD
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
=======
from random import randint, choice
from brain_games.cli import welcome_user
def gcd_code(num1,num2):
    divider1 = []
    divider2 = []
    result =[]
    for i in range(1,num1 +1 ):
        if num1 % i == 0:
            divider1.append(i)
    for j in range(1,num2 + 1):
>>>>>>> 011fcd61951bfb5304d0300577077a42bd8e14d5
        if num2 % j == 0:
            divider2.append(j)
    for k in divider1:
        if k in divider2:
            result.append(k)
    return max(result)
<<<<<<< HEAD


=======
>>>>>>> 011fcd61951bfb5304d0300577077a42bd8e14d5
def gcd_game():
    name = welcome_user()
    print("Find the greatest common divisior of given numbers.")
    count = 0
    while count <3:
<<<<<<< HEAD
        num1 = randint(1, 101)
        num2 = randint(1, 101)
=======
        num1 = randint(1,101)
        num2 = randint(1,101)
>>>>>>> 011fcd61951bfb5304d0300577077a42bd8e14d5
        print(f'Question: {num1} {num2}')
        n = int(input('yor answer: '))
        if gcd_code(num1,num2) == n:
            print('Correct!')
<<<<<<< HEAD
            count += 1
=======
            count +=1
>>>>>>> 011fcd61951bfb5304d0300577077a42bd8e14d5
        else:
            print(f"{n} is wrong answer ;(. Correct answer was {gcd_code(num1,num2)}.")
            print(f"let's try again,{name}")
    if count == 3: 
<<<<<<< HEAD
        print(f'congratulations, {name}')


=======
        print (f'congratulations, {name}')

     
>>>>>>> 011fcd61951bfb5304d0300577077a42bd8e14d5
if __name__ == '__main__':
    gcd_game()