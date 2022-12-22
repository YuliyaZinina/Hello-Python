import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

# Выберете команду:
#           1 - показать всех сотрудников\n'
#           2 - добавить сотрудника
#           3 - Изменить данные сотрудника\n'
#           4 - удалить сотрудника'
#           5 - экспортировать в файл
#           6 - импортировать из файла


def main():
    select = view.show_menu()
    if select == 1:
        logging.info('Выбран пункт меню 1')
        employees = model.get_list()
        view.show_employees(employees)
        logging.info('Список сотрудников выведен на экран')
    elif select == 2:
        logging.info('Выбран пункт меню 2')
        new_employee = view.add_employee()
        model.add_employee(new_employee)
        logging.info('Новые данные добавлены')
    elif select == 3:
        logging.info('Выбран пункт меню 3')
        number, data = view.change_employee()
        model.update_employees(number, data)
        logging.info('Данные обновлены')
    elif select == 4:
        logging.info('Выбран пункт меню 4')
        number = view.delete_employee()
        model.delete_employee(number)
        logging.info('Данные сотрудника удалены')
    elif select == 5:
        logging.info('Выбран пункт меню 5')
        view.export_all_in_file()
        model.list_export_in_file()
        logging.info('Список сотрудников выгружен в файл')
    elif select == 6:
        logging.info('Выбран пункт меню 6')
        view.import_from_file()
        model.list_import_from_file()
        logging.info('Список сотрудников загружен из файла')
