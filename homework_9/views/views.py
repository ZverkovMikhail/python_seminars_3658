from telegram import Update, ParseMode

from homework_9 import models
from homework_9.views import keyboards


def get_contacts_list():
    text = ''
    entries = models.get_peoples()

    if entries:
        for idx, entry in enumerate(entries, 1):
            text += f"{idx} - {entry['l_name']} {entry['f_name']}\n"
    else:
        text = 'Записей нет!'
    return text


def start(update, context):
    if update.callback_query:
        msg = update.callback_query.message.edit_text
    else:
        msg = update.message.reply_text

    msg('*Телефонный справочник*\n' + get_contacts_list(),
        reply_markup=keyboards.phones(),
        parse_mode=ParseMode.MARKDOWN
        )


def choice_contact(update, context, error=False):
    if update.callback_query:
        msg = update.callback_query.message.edit_text
    else:
        msg = update.message.reply_text
        remove_reply_markup_from_prev_msg(update)
    msg(
        get_contacts_list() +
        'Введите номер контакта' if not error else 'Вы ввели не корректные данные!\n Попробуйте снова',
        reply_markup=keyboards.choice()
    )


def add_contact(update, context, error=False):
    if update.callback_query:
        msg = update.callback_query.message.edit_text
    else:
        msg = update.message.reply_text
        remove_reply_markup_from_prev_msg(update)
    msg(
        'Введите Имя и Фамилию через запятую' if not error else 'Вы ввели не корректные данные!\n Попробуйте снова',
        reply_markup=keyboards.choice()
    )


def add_contact_number(update, context, error=False):
    if update.callback_query:
        msg = update.callback_query.message.edit_text
    else:
        msg = update.message.reply_text
        remove_reply_markup_from_prev_msg(update)
    msg(
        'Введите Номер телефона и Описание через пробел' if not error else 'Вы ввели не корректные данные!\n Попробуйте снова',
        reply_markup=keyboards.add_phone_number()
    )


def find(update, context, error=False):
    if update.callback_query:
        msg = update.callback_query.message.edit_text
    else:
        msg = update.message.reply_text
        remove_reply_markup_from_prev_msg(update)
    msg(
        'Введите Фамилию для поиска' if not error else 'Ничего не найдено!\n Попробуйте снова',
        reply_markup=keyboards.choice()
    )


def contact_menu(update: Update, context):
    contact = context.user_data['contact']
    numbers = context.user_data['numbers']
    text = f"{contact['f_name']} {contact['l_name']}\n"
    for num in numbers:
        text += f"{num['number']} {num['description']}\n"

    if update.callback_query:
        msg = update.callback_query.message.edit_text
    else:
        msg = update.message.reply_text
    msg(text, reply_markup=keyboards.contact())


def delete_contact(update: Update, context):
    if update.callback_query:
        msg = update.callback_query.message.edit_text
    else:
        msg = update.message.reply_text
        remove_reply_markup_from_prev_msg(update)
    contact = context.user_data['contact']
    msg(
        f"Вы уверены что ходите удалить {contact['f_name']} {contact['l_name']} из списка контактов",
        reply_markup=keyboards.delete()
    )

def remove_reply_markup_from_prev_msg(update):
    update.message.bot.edit_message_reply_markup(
        chat_id=update.message.chat_id,
        message_id=update.message.message_id - 1
    )
