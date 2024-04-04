from random import randint


DESCRIPTION = 'What number is missing in the progression?'


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
    start = randint(1, 11)
    step = randint(1, 11)
    length = randint(5, 11)
    random_index = randint(0, length - 1)
    collection = progression_generator(start, step, length)
    collection_with_dots, correct_answer = index_progression(collection, random_index)
    question = ' '.join(str(num) for num in collection_with_dots)
    return question, correct_answer
    