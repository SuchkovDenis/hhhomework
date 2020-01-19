from random import randint
from types import GeneratorType


def gen(n):
    """
    Генераторная функция, которая принимает число N возвращает N рандомных чисел от 1 до 100
    :param n: размер гененратора
    :return: генератор случайных чисел
    """
    for i in range(n):
        yield randint(1, 100)


# генераторное выражение, которое делает то же самое
gen_lambda = lambda n: (randint(1, 100) for i in range(n))


if __name__ == '__main__':
    N = 3
    generator1 = gen(N)
    assert isinstance(generator1, GeneratorType) and len(list(generator1)) == N

    generator2 = gen_lambda(N)
    assert isinstance(generator2, GeneratorType) and len(list(generator2)) == N
