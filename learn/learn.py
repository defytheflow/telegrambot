""" This module consists of learning commands. """
import json
import random

import telegram.ext

from decorators import send_action


@send_action(telegram.ChatAction.TYPING)
def learn(update, context):
    """
        This function displays all the available commands for 'learn' module.
    """
    keyboard = [["/fact"]]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True,
                                                one_time_keyboard=True, selective=True)
    text = "Knowledge is true power! Let's see what we can learn today!"
    context.bot.send_photo(update.message.chat_id, photo=open("static/img/photo/learn-steve.jpg", "rb"))
    context.bot.send_message(update.message.chat_id, text=text, reply_markup=reply_markup)


@send_action(telegram.ChatAction.TYPING)
def fact(update, context):
    with open("data/json/facts.json") as file:
        facts = json.load(file)
    random_fact = random.choice(facts)
    context.bot.send_message(update.message.chat_id, text=f"{random_fact}",
                             parse_mode=telegram.ParseMode.MARKDOWN)
