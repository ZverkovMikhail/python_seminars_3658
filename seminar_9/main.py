import logging
import config as conf
import calculate as c

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = conf.get_token()


def start(update, context):
    update.message.reply_text(
        "Привет. Я бот калькулятор!\n"
        f"Поддерживаю следующие операции: {', '.join(c.math.keys())} над двумя числами")
    return 0


def calc(update, context):
    answer = c.calc(update.message.text)
    answer = answer if answer else 'Вы ввели не правильные данные, возможно данная операция не поддерживается!'
    update.message.reply_text(answer)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)
    calc_handler = MessageHandler(Filters.text & ~Filters.command, calc)
    dp.add_handler(start_handler)
    dp.add_handler(calc_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
