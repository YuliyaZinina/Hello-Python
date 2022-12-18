# общение с пользователем
import controller as c


def to_do():
    a = int(input('Введите 1 - для импорта из файла, 2 - для экспорта в файл: '))
    return a


def print_result():
    print(c.result())
