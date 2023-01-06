import models
from my_token import token
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = token


def start(update, context):
    update.message.reply_text(
        'Привет! Выберите действие:\n'
        '/show - показать всех сотрудников\n'
        '/add - добавить сотрудника\n'
        '/update - изменить данные сотрудника\n'
        '/delete - удалить данные сотрудника\n'
        '/stop - закончить диалог')


def show(update, context):
    update.message.reply_text(
        'Вот список всех сотрудников:\n')
    employees = models.get_list()
    text = ''
    for i, employee in enumerate(employees):
            text += f'{i}, {employee}\n'
    update.message.reply_text(f'{text}')


def add(update, context):
    update.message.reply_text('Введите Фамилию, Имя, Телефон и Должность через пробел')
    return 1


def add_to_list(update, context):
    try:
        data = update.message.text.split()
        models.add_employee(data)
        update.message.reply_text('Данные добавлены')
    except Exception:
        update.message.reply_text('Введите данные верно')


update_data = []


def update_list_what_line(update, context):
    update.message.reply_text('Введите номер строки для перезаписи')
    return 1


def update_list_what_data(update, context):
    try:
        update_data.append(update.message.text)
        update.message.reply_text('Введите измененные данные через пробел (Фамилия Имя Номер_телефона Должность)')
        return 2
    except Exception:
        update.message.reply_text('Введите натуральное число')


def update_list(update, context):
    try:
        update_data.append(update.message.text)
        number = int(update_data[0])
        data = update_data[1].split()
        models.update_employees(number, data)
        update.message.reply_text('Данные добавлены')
    except Exception:
        update.message.reply_text('Введите данные верно')


def delete_list_what_line(update, context):
    update.message.reply_text('Введите номер строки для удаления')
    return 1


def delete_line(update, context):
    try:
        number = int(update.message.text)
        models.delete_employee(number)
        update.message.reply_text('Данные удалены')
    except Exception:
        update.message.reply_text('Введите натуральное число')


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)
    show_handler = CommandHandler('show', show)

    add_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, add_to_list)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    update_handler = ConversationHandler(
        entry_points=[CommandHandler('update', update_list_what_line)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, update_list_what_data)],
            2: [MessageHandler(Filters.text & ~Filters.command, update_list)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', delete_list_what_line)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, delete_line)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(start_handler)
    dp.add_handler(show_handler)
    dp.add_handler(add_handler)
    dp.add_handler(update_handler)
    dp.add_handler(delete_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
