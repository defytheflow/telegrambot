""" This module consists of entertainment commands. """

import telegram.ext

from decorators import send_action


@send_action(telegram.ChatAction.TYPING)
def entertain(update, context):
    """
        This function displays all the available commands for 'entertain' module.
    """
    keyboard = [["/party"]]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True,
                                                one_time_keyboard=True, selective=True)
    text = "Let's have some fun then!"
    context.bot.send_photo(update.message.chat_id, photo=open("static/img/photo/entertain-steve.jpeg", "rb"))
    context.bot.send_message(update.message.chat_id, text=text, reply_markup=reply_markup)


@send_action(telegram.ChatAction.TYPING)
def party(update, context):
    context.bot.send_animation(update.message.chat_id, animation=open("static/animation/party.gif", "rb"))