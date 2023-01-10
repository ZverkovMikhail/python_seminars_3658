from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, \
    ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, \
    CallbackContext

from config import get_token

start_menu = ReplyKeyboardMarkup([['/start']], resize_keyboard=True)
active_menu = ReplyKeyboardMarkup([['/help'], ['/restart']], resize_keyboard=True)
throw_waiting_menu = ReplyKeyboardMarkup([['/help']], resize_keyboard=True)
dice_menu = InlineKeyboardMarkup([[InlineKeyboardButton('Бросить кубик', callback_data='dice')]])
is_bot_turn = False
is_started = False
candies = 0
steps = 0


def start(update: Update, context: CallbackContext, is_first=True):
    global candies
    global steps

    if is_first:
        update.effective_chat.send_message(
            f'*{update.effective_user.username},* приветствую вас!\n'
            f'*Данный бот предназначен для игры в конфетки!*\n'
            f'_* чтобы ознакомиться с правилами нажмите кнопку /help *_ \n'
            'для начала игры брости кубик для определения первого хода(4-6 ваш ход первый)',
            reply_markup=throw_waiting_menu,
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        update.effective_chat.send_message(
            f'Хочешь попробовать еще? 😁',
            reply_markup=throw_waiting_menu,
            parse_mode=ParseMode.MARKDOWN
        )
    update.effective_chat.send_message(
        'Ну что, давай сыграем в конфетки!!!',
        reply_markup=dice_menu
    )
    candies = 50
    steps = 15


def dice_roll(update: Update, context: CallbackContext):
    global is_bot_turn
    global is_started
    print(update.callback_query.message)
    update.callback_query.message.edit_reply_markup()
    dice_value = update.effective_chat.send_dice().dice.value

    is_bot_turn = dice_value < 4
    is_started = True
    if is_bot_turn:
        update.effective_chat.send_message(
            'Жаль, но бот ходит первым!)',
            reply_markup=active_menu
        )
        bot_turn(update, context)
    else:
        update.effective_chat.send_message(
            f'Поздравляю, Ваш ход!\n На кону {candies} конфет\nвведите количество конфет(1-{steps})',
            reply_markup=active_menu
        )


def turn(update: Update, context: CallbackContext):
    global candies
    global is_bot_turn
    global is_started
    if is_started:
        try:
            player_turn(update, context)
            check_win(update, context)
            bot_turn(update, context)
            check_win(update, context)
            update.effective_chat.send_message(
                f'Ваш ход!\nвведите количество конфет(1-{steps})'
            )
        except ValueError:
            update.effective_chat.send_message(
                f'Вы ввели не верное значение!\nвведите количество конфет(1-{steps})'
            )
        except Exception as e:
            print(e)
            if is_bot_turn:
                update.effective_chat.send_message(
                    f'Сожалею, но победил бот!(('
                )
            else:
                update.effective_chat.send_message(
                    'Поздравляю, вы победили!!! 🥳🥳🥳'
                )
            is_started = False
            start(update, context, is_first=False)

    else:
        update.effective_chat.send_message(
            f'Для начала брось кубик ☝️'
        )


def bot_turn(update: Update, context: CallbackContext):
    global candies
    global steps
    global is_bot_turn
    is_bot_turn = True
    candy = candies % (steps + 1)

    candy = 1 if candy == 0 else candy

    if candies <= steps:
        candy = candies
    candies -= candy
    update.effective_chat.send_message(f'Бот взял {candy} конфет\n На кону {candies} конфет')


def player_turn(update: Update, context: CallbackContext):
    global steps
    global candies
    global is_bot_turn
    is_bot_turn = False
    candy = int(update.message.text)
    if steps < candy < 1:
        raise ValueError
    else:
        candies -= candy
        update.effective_chat.send_message(
            f'Вы взяли {candy}\n На кону {candies} конфет\n теперь ходит бот'
        )


def check_win(update, context):
    global candies
    if candies <= 0:
        raise Exception('win')


def help_msg(update, context):
    update.effective_chat.send_message(
        f'На столе лежит определенное количество конфет,\n'
        f'каждый по очереди берет от 1 до {steps} конфет,\n '
        f'побеждает тот, кто заберет последние конфеты со стола!'
    )


def init():
    updater = Updater(get_token())
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('restart', start))
    dp.add_handler(CommandHandler('help', help_msg))
    dp.add_handler(CallbackQueryHandler(dice_roll))
    dp.add_handler(MessageHandler(Filters.text, turn))
    updater.start_polling()
    updater.idle()
