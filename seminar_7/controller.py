# Обработка входных данных
import view as v
import model_txt as mt

task = v.to_do()


def result():
    phonebook_list = ['Медведев', 'Иван', '098765', 'домашний', 'Чугов', 'Евгений', '987654', 'рабочий','Меринов', 'Стас', '876543', 'личный']
    file = 'phonebook.txt'
    if task == 1:
        mt.txt_import(file, phonebook_list)
        return phonebook_list
    elif task == 2:
        mt.txt_export(file, phonebook_list)
        return 'Файл записан'


v.print_result()
