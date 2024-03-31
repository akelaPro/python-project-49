from random import randint
from brain_games.cli import welcome_user

def progression_generator(first, end, length):
    generator = []
    for i in range(length):
        generator.append(first)
        first += end
    return generator


def index_progression(collection, index):
    collection_copy = collection.copy()
    index_prog = collection_copy[index]
    collection_copy[index] = '..'
    return collection_copy, index_prog


def progress_game():
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 0

    while count < 3:
        start = randint(1, 11)
        step = randint(1, 11)
        length = randint(5, 11)
        random_index = randint(0, length - 1)
        collection = progression_generator(start, step, length)
        collection_with_dots, correct_input = index_progression(collection, random_index)
        question = ' '.join(str(num) for num in collection_with_dots)
        print(f'Question: {question}')
        user_input = input('Your answer: ')
        if user_input == str(correct_input):
            print('Correct!')
            count += 1
        else:
            print(f"{user_input} is wrong answer ;(. Correct answer was {correct_input}.")
            print(f"Let's try again, {name}")
            count = 0
        if count == 3:
            print(f'Congratulations, {name}!')

if __name__ == '__main__':
    progress_game()
