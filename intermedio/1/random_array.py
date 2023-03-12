from random import randint


def get_random_array(array_from=5000, array_to=10000, integer_from=-50000, integer_to=50000):
    array = []
    size = randint(array_from, array_to)
    for i in range(size):
        array.append(randint(integer_from, integer_to))
    return array
