from decorators import cache_decorator


class UnsupportedOperationError(Exception):
    pass


@cache_decorator
def calculator(a, b, operation):
    """
    Функция, производящая арифметическую операцию operation
    над введенными числами a и b.
    Так как функция может быть использована не только в этом месте,
    но и вызывана откуда-то еще, то решил ее сделать ответсвенной
    только за произведение вычислений. В случае некорректности
    введенных данных выбрасываются исключения. Для нашего консольного
    случая сделал отдельные функции, обрабатывающие некорректный ввод
    :param a: первое число
    :param b: второе число
    :param operation: арифметическая операция
    :return: результат арифметической операции над переданными числами
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y,
    }

    if type(a) != int or type(b) != int:
        raise ValueError('Переданные числа не являются натуральными')

    if operation not in operations:
        raise UnsupportedOperationError('Операция не поддерживается,'
                                        'используйте следующие: +, -, /, *, **')

    return operations[operation](a, b)


def safe_int_input():
    """
    Функция, гарантирующая ввод через консоль натурального числа.
    :return: натуральное число
    """
    while True:
        try:
            return int(input('Введите число: '))
        except ValueError:
            print('Введенное число не является натуральным. Попробуйте еще')


def available_operation_input():
    """
    Функция, гарантирующая ввод через консоль
    доступной арифметической операции.
    :return: доступная в нашем калькуляторе арифметическая операция
    """
    available_operations = {'+', '-', '/', '*', '**'}
    operation = input('Введите операцию: ')

    while operation not in available_operations:
        operation = input('Введенная операция неподдерживается, '
                          'введите одну из следующих: +, -, /, *, **: ')

    return operation


if __name__ == '__main__':
    while True:
        number1 = safe_int_input()
        number2 = safe_int_input()
        op = available_operation_input()

        try:
            print('Результат: ', calculator(number1, number2, op))
        except ZeroDivisionError:
            print('Невозможно произвести вычисления: на 0 делить нельзя')
        print("-"*10)
