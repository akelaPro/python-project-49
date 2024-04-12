from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def progression_generator(first, step, length):
    generator = []
    for _ in range(length):
        generator.append(first)
        first += step
    return generator


def index_progression(collection, index):
    collection_copy = collection.copy()
    index_prog = collection_copy[index]
    collection_copy[index] = '..'
    return collection_copy, index_prog


def generate_round():
    start = randint(1, 11)
    step = randint(1, 11)
    length = randint(5, 10)
    random_index = randint(0, length - 1)
    collection = progression_generator(start, step, length)
    with_dots, correct_answer = index_progression(collection, random_index)
    question = ' '.join(str(num) for num in with_dots)
    return question, correct_answer
