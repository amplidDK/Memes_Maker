import time
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    update.message.reply_text('С подключением %username%')
    time.sleep(2)
    update.message.reply_text('Хм...Простите')
    update.message.reply_text(f'С подключением, {update.message.from_user.first_name}!')
    update.message.reply_text('К сожалению, я могу пока только зеркалить ваши сообщения.\n'
                              'Надеюсь скоро мой ленивый создатель соизволит что-то допилить.\n'
                              'А пока "наслаждайтесь" тем, что есть =)')


def answer_user(update, context):
    text = update.message.text
    update.message.reply_text(text)

def main():
    # Передаем ключ
    bot = Updater(settings.API_KEY, use_context=True)

    # Накидываем обработчики событий
    disp = bot.dispatcher
    disp.add_handler(CommandHandler('start', greet_user))
    disp.add_handler(MessageHandler(Filters.text, answer_user))

    # Отправляем бота в телегу для проверки обновлений
    bot.start_polling()

    # Запускаем бота
    bot.idle()

if __name__ == '__main__':
    main()
