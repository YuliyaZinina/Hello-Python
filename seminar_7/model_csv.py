# Основные операции с csv
import csv


def csv_import(file):
    with open(file, encoding="utf8") as data:
        phone_list = list(csv.reader(data, delimiter=','))
    return phone_list


def csv_export(file, phone_list):
    with open(file, mode="w", encoding='utf-8') as data:
        file_writer = csv.writer(data, delimiter=",", lineterminator="\r")
        for row in phone_list:
            file_writer.writerow(row)
