from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

from config import get_token
from homework_9 import models
from homework_9.views import views
from homework_9.views import callback_commands as cc

CONTACTS_MENU, CHOICE_CONTACT, CONTACT_MENU, \
FIND_BY_LAST_NAME, ADD_CONTACT_NAME, ADD_CONTACT_NUMBER, DELETE_CONTACT = range(7)


def cancel(update: Update, context) -> int:
    """Cancels and ends the conversation."""

    user = update.message.from_user
    update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def start(update, context):
    views.start(update, context)
    return CONTACTS_MENU


def contacts_menu_handler(update: Update, context):
    match update.callback_query.data:
        case cc.choice_contact:
            views.choice_contact(update, context)
            return CHOICE_CONTACT

        case cc.add_contact:
            views.add_contact(update, context)
            return ADD_CONTACT_NAME

        case cc.back:
            start(update, context)
            return CONTACTS_MENU

        case cc.find:
            views.find(update, context)
            return FIND_BY_LAST_NAME


def choice_contact_handler(update: Update, context):
    if update.callback_query and update.callback_query.data == cc.back:
        views.start(update, context)
        return CONTACTS_MENU
    try:
        contact = models.get_people_by_num(int(update.message.text))
        numbers = models.get_phone_numbers(contact['id'])
        context.user_data['contact'] = contact
        context.user_data['numbers'] = numbers
    except Exception as e:
        print(e)
        views.choice_contact(update, context, True)
        return CHOICE_CONTACT

    views.remove_reply_markup_from_prev_msg(update)
    views.contact_menu(update, context)
    return CONTACT_MENU


def contact_menu_handler(update: Update, context):

    match update.callback_query.data:

        case cc.delete:
            views.delete_contact(update, context)
            return DELETE_CONTACT

        case cc.back:
            start(update, context)
            return CONTACTS_MENU

    return CONTACT_MENU


def add_contact_name_handler(update: Update, context):
    text = update.message.text
    try:
        f_name, l_name = text.split(' ')
        contact_id = models.create_people(f_name, l_name)
        context.user_data['contact_id'] = contact_id
        views.add_contact_number(update, context)
        return ADD_CONTACT_NUMBER
    except Exception:
        views.add_contact(update, context, True)
        return ADD_CONTACT_NAME


def add_contact_number_handler(update: Update, context):
    if update.callback_query and update.callback_query.data == cc.end:
        views.start(update, context)
        return CONTACTS_MENU
    else:
        text = update.message.text
        try:
            phone, description = text.split(' ')
            models.add_phone_number(
                context.user_data['contact_id'],
                phone,
                description
            )
            views.add_contact_number(update, context)
            return ADD_CONTACT_NUMBER
        except Exception:
            views.add_contact_number(update, context, True)
            return ADD_CONTACT_NUMBER


def delete_contact_handler(update: Update, context):
    match update.callback_query.data:

        case cc.yes:
            models.delete_people(context.user_data['contact']['id'])
            views.start(update, context)
            return CONTACTS_MENU

        case cc.back:
            views.contact_menu(update, context)
            return CONTACT_MENU


def find_contact_handler(update: Update, context):
    if update.callback_query and update.callback_query.data == cc.back:
        views.start(update, context)
        return CONTACTS_MENU

    last_name = update.message.text
    contact = models.find_contact_by_last_name(last_name)
    if contact:
        views.remove_reply_markup_from_prev_msg(update)
        numbers = models.get_phone_numbers(contact['id'])
        context.user_data['contact'] = contact
        context.user_data['numbers'] = numbers
        views.contact_menu(update, context)
    else:
        views.find(update, context, True)
        return FIND_BY_LAST_NAME


def init():
    updater = Updater(get_token())
    dp = updater.dispatcher

    menu_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CONTACTS_MENU: [CallbackQueryHandler(contacts_menu_handler)],
            FIND_BY_LAST_NAME: [MessageHandler(Filters.text, find_contact_handler),
                                CallbackQueryHandler(find_contact_handler)],
            CHOICE_CONTACT: [MessageHandler(Filters.text, choice_contact_handler),
                             CallbackQueryHandler(choice_contact_handler)],
            CONTACT_MENU: [CallbackQueryHandler(contact_menu_handler)],
            ADD_CONTACT_NAME: [MessageHandler(Filters.text, add_contact_name_handler)],
            ADD_CONTACT_NUMBER: [MessageHandler(Filters.text, add_contact_number_handler),
                                 CallbackQueryHandler(add_contact_number_handler)],
            DELETE_CONTACT: [CallbackQueryHandler(delete_contact_handler)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    dp.add_handler(menu_handler)
    updater.start_polling()
    updater.idle()
