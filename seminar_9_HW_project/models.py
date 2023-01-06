import csv


def get_list():
    with open('list.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        # title = next(reader)
        return list(reader)


def add_employee(entry):
    with open('list.csv', mode="a", encoding='utf-8') as data:
        file_writer = csv.writer(data, delimiter=",", lineterminator="\r\n")
        file_writer.writerow(entry)


def update_employees(number, data):
    try:
        with open('list.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            actual_data = list(reader)
            actual_data[number] = data
            print(actual_data[number])
        with open('list.csv', mode="w", encoding='utf-8') as data:
            file_writer = csv.writer(data, delimiter=",", lineterminator="\r\n")
            for i in actual_data:
                file_writer.writerow(i)
    except IndexError:
        print('Вы вышли за границу списка')
        exit()
    except Exception:
        print('Появились какие-то ошибки')


def delete_employee(number):
    try:
        with open('list.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            actual_data = list(reader)
            del actual_data[number]
        with open('list.csv', mode="w", encoding='utf-8') as data:
            file_writer = csv.writer(data, delimiter=";", lineterminator="\r\n")
            for i in actual_data:
                file_writer.writerow(i)
    except IndexError:
        print('Вы вышли за границу списка')
        exit()
    except Exception:
        print('Появились какие-то ошибки')

