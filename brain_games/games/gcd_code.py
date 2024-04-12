from random import randint


from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
