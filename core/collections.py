def even(some_not_even_list):
    """
    Создает новый список с четными элементами из списка some_not_even_list
    :param some_not_even_list: входной список
    :return: список четных чисел из входного списка
    """
    return [x for x in some_not_even_list if x % 2 == 0]


def get_ages(some_years_of_birth):
    """
    Создает список возрастов в 2014 году по переданному списку годов рождения
    без использования циклов
    :param some_years_of_birth: переданный список годов рождения
    :return: список возрастов для каждого года рождения
    """
    return [2014 - x for x in some_years_of_birth]


def get_first_n_last(some_list):
    """
    Создает новый список, состоящий из первого и последнего элемента переданного списка
    :param some_list: входной список
    :return: список, состоящий из первого и последнего элемента
    """
    return [some_list[0], some_list[-1]]


def get_list_without_repetition(some_list):
    """
    Функция, которая принимает список и возвращает новый список,
    состоящий из элементов принятого, но без повторений
    :param some_list: входной список
    :return: список, состоящий из элементов принятого, но без повторений
    """
    return list(set(some_list))


def map_keys_and_values(some_keys, some_values):
    """
    Функция, которая возвращает словарь,
    ключи которого из списка some_keys, а значения из списка some_values
    :param some_keys: клчи
    :param some_values: значения
    :return: словарь
    """
    return dict(zip(some_keys, some_values))


def count_symbols(some_string):
    """
    Функция, которая принимает строку и возвращает словарь состоящий из
    ключей - символов из строки,
    значений - количество повторений этих символов в строке
    :param some_string: входная строка
    :return: словарь частот символов в строке
    """
    counter = {}
    for x in some_string:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1
    return counter


if __name__ == '__main__':
    not_even_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = [4, 16, 36, 64, 100]
    assert even_list == even(not_even_list)

    years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
    ages = [24, 23, 24, 24, 22, 23]
    assert ages == get_ages(years_of_birth)

    numbers = [5, 10, 15, 20, 25]
    first_n_last = [5, 25]
    assert first_n_last == get_first_n_last(numbers)

    list_with_repetition = [1, 1, 3, 4, 2, 2, 2, 6]
    set_from_list = {1, 2, 3, 4, 6}
    assert set_from_list == set(get_list_without_repetition(list_with_repetition)) \
           and list == type(list_with_repetition)

    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#00FF00', '#0000FF']
    dictionary = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
    assert dictionary == map_keys_and_values(keys, values)

    s = 'some string'
    frequency_dictionary = {'s': 2, 'o': 1, 'm': 1, 'e': 1, ' ': 1,
                            't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
    assert frequency_dictionary == count_symbols(s)
