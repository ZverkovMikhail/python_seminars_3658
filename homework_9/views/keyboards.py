from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from homework_9.views import callback_commands as cc


def choice():
    keyboard = [
        [InlineKeyboardButton('<< Назад', callback_data=cc.back)],
    ]
    return InlineKeyboardMarkup(keyboard)


def add_phone_number():
    keyboard = [
        [InlineKeyboardButton('Завершить добавление телефонов', callback_data=cc.end)],
    ]
    return InlineKeyboardMarkup(keyboard)


def phones():
    keyboard = [
        [InlineKeyboardButton('Выбрать контакт', callback_data=cc.choice_contact)],
        [InlineKeyboardButton('Добавить контакт', callback_data=cc.add_contact)],
        [InlineKeyboardButton('Поиск', callback_data=cc.find)],
    ]
    return InlineKeyboardMarkup(keyboard)


def contact():
    keyboard = [
        [InlineKeyboardButton('Удалить', callback_data=cc.delete)],
        [InlineKeyboardButton('<< Назад', callback_data=cc.back)],
    ]
    return InlineKeyboardMarkup(keyboard)


def delete():
    keyboard = [
        [InlineKeyboardButton('Да', callback_data=cc.yes)],
        [InlineKeyboardButton('<< Назад', callback_data=cc.back)],
    ]
    return InlineKeyboardMarkup(keyboard)
