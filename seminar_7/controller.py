# Обработка входных данных
import view as v
import model_txt as mt
import model_csv as mc

task = v.to_do()


def result():
    phonebook_list = [['Медведев', 'Иван', '098765', 'домашний'], ['Чугов', 'Евгений', '987654', 'рабочий'],['Меринов', 'Стас', '876543', 'личный']]
    if task == 1 or task == 2:
        file = 'phonebook.txt'
        if task == 1:
            mt.txt_import(file, phonebook_list)
            return phonebook_list
        elif task == 2:
            mt.txt_export(file, phonebook_list)
            return 'Файл txt записан'
    elif task == 3 or task == 4:
        file = 'phonebook_csv.csv'
        if task == 3:
            phonebook_list = mc.csv_import(file)
            return phonebook_list
        elif task == 4:
            mc.csv_export(file, phonebook_list)
            return 'Файл csv записан'


v.print_result()
