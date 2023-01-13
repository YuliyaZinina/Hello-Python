from my_token import token

import logging
import random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

reply_keyboard = [['/play', '/setting'],
                  ['/rules', '/close_keyboard']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard_play = [['/rules', '/stop']]

markup_play = ReplyKeyboardMarkup(reply_keyboard_play, one_time_keyboard=False)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = token


candies = 50
step = 15


def start(update, context):
    name = f'{update.message.from_user.first_name}'
    update.message.reply_text(
        f'Привет, {name}! Давай поиграем в игру с конфетами!\n'
        'Нажми /play, чтобы начать прямо сейчас,\n'
        '/setting, чтобы настроить исходные данные\n'
        '/rules, чтобы почитать правила,\n'
        '/close_keyboard, чтобы закрыть клавиатуру,\n'
        '/stop, чтобы завершить нашу беседу',
        reply_markup=markup
    )


def setting(update, context):
    update.message.reply_text(
        'Введите количество конфет на кону и максимальноре количество на один ход через пробел')
    return 1


def set_setting(update, context):
    global candies
    global step
    candies, step = map(int, update.message.text.split())
    update.message.reply_text('Настройки изменены, жми /play!', reply_markup=markup_play)
    return ConversationHandler.END


def rules(update, context):
    update.message.reply_text(
        'На столе лежит 50 конфет. Играют два игрока делая ход друг после друга.'
        'За один ход можно забрать не более 15 конфет.'
        'Выигрывает тот, кто делает ход последним. Кстати, исходные данные можно изменить в настройках',
        reply_markup=markup
    )


def play(update, context):
    update.message.reply_text(
        f'Да начнётся игра!\n'
        f'Итак, на столе {candies} конфет, ты можешь взять не больше {step}\n'
        'Дам тебе фору, ходи первым! Сколько возьмёшь?',
        reply_markup=markup_play
    )
    return 1


def play_step(update, context):
    global candies
    global step
    try:
        candy = int(update.message.text)
    except Exception:
        update.message.reply_text(f'Что-то не так! Введи значение верно. Можно взять от 1 до {step} конфет.',
                                  reply_markup=markup_play)

    if candy > step or candy < 0:
        update.message.reply_text(f'Можно взять от 1 до {step} конфет, введи значение верно', reply_markup=markup_play)
    else:
        candies -= candy

        if candies <= step:
            update.message.reply_text(
                f'Осталось {candies} конфет. Я забираю оставшиеся конфеты, я победил!\nИгра окончена!',
                reply_markup=markup)
            context.bot.send_photo(update.effective_chat.id, photo=open('bot_win.jpg', 'rb'))
            candies = 50
            step = 15
            return ConversationHandler.END
        else:
            bots_step = random.randint(1, step)
            update.message.reply_text(f'На столе {candies} конфет, я забираю {bots_step}, осталось {candies-bots_step}.\n'
                                      f'Твой ход!', reply_markup=markup_play)
            candies -= bots_step
            if candies <= step:
                update.message.reply_text('Тут и так всё ясно! Поздравляю! Ты победил!\nИгра окончена!',
                                          reply_markup=markup)
                context.bot.send_animation(update.effective_chat.id, animation=open('you_win.gif', 'rb'))
                candies = 50
                step = 15
                return ConversationHandler.END


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def stop(update, context):
    global candies
    global step
    update.message.reply_text(
        'Пока! Надумаешь поиграть, просто напиши мне /start', reply_markup=ReplyKeyboardRemove())
    candies = 50
    step = 15
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    setting_handler = ConversationHandler(
        entry_points=[CommandHandler('setting', setting)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_setting)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_step)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(play_handler)
    dp.add_handler(setting_handler)
    dp.add_handler(CommandHandler('rules', rules))
    dp.add_handler(CommandHandler('close_keyboard', close_keyboard))
    dp.add_handler(CommandHandler('stop', stop))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
