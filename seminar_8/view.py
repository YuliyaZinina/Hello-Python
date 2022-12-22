
def show_menu():
    print('Выберете команду:\n1 - показать всех сотрудников\n'
          '2 - добавить сотрудника\n3 - Изменить данные сотрудника\n'
          '4 - удалить сотрудника\n5 - экспортировать в файл\n'
          '6 - импортировать из файла')
    try:
        select = int(input())
        if select not in [1, 2, 3, 4, 5, 6]:
            raise ValueError
        return select
    except Exception:
        print('Что-то не так!')
        exit()


def show_employees(list):
    print('Список всех сотрудников: ')
    for i, employee in enumerate(list):
        print(i, *employee)


def add_employee():
    print('Введите Фамилию, Имя, Телефон и Должность через пробел: ')
    data = input().split()
    return data


def change_employee():
    print('Выберете номер строки для перезаписи: ')
    number = int(input())
    print('Введите измененные данные: ')
    new_data = input().split()
    return number, new_data


def delete_employee():
    print('Введите номер строки для удаления: ')
    number = int(input())
    return number


def export_all_in_file():
    print('Данные будут выгружены в файл')


def import_from_file():
    print('Данные будут загружены из файла')