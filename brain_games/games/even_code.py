from random import randint



DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), correct_answer
    

if __name__ == '__main__':
    generate_round()