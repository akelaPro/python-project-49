from random import randint, choices

DESCRIPTION = 'What is the result of the expression?'


def calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def generate_round():
    operations = ['+', '-', '*']
    a = randint(1, 100)
    b = randint(1, 100)
    operation = choices(operations)
    question = f"{a} {operation} {b}"
    correct_answer = str(calc(a, b, operation))
    return question, correct_answer

if __name__ == '__main__':
    generate_round()