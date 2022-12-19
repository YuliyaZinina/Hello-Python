# общение с пользователем
import controller as c


def to_do():
    a = int(input('Введите 1 - для импорта из файла txt, 2 - для экспорта в файл txt,\n3 - для импорта из файла csv, 4 - для экспорта в файл csv: '))
    return a


def print_result():
    print(c.result())
