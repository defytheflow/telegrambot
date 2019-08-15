""" This module has got all the repeating automated commands that run all the time. """

import os
import json
import random

import telegram.ext

from settings import GROUP_CHAT_ID


def wake_up(context: telegram.ext.CallbackContext):
    context.bot.send_message(GROUP_CHAT_ID, text="Woke up")
    context.bot.send_animation(GROUP_CHAT_ID, animation=open("static/animation/wake-up.gif", "rb"))


def daily_quote(context: telegram.ext.CallbackContext):
    with open("data/json/quotes.json", encoding="cp1251") as file:
        quotes = json.load(file)
    random_quote = random.choice(quotes)
    quote_text = random_quote["quoteText"]
    quote_author = random_quote["quoteAuthor"]
    context.bot.send_message(GROUP_CHAT_ID, text=f"*{quote_text}*\n\n*{quote_author}*",
                             parse_mode=telegram.ParseMode.MARKDOWN)


def daily_fact(context: telegram.ext.CallbackContext):
    with open("data/json/facts.json") as file:
        facts = json.load(file)
    random_fact = random.choice(facts)
    context.bot.send_message(GROUP_CHAT_ID, text=f"*Daily fact.*\n\n{random_fact}",
                             parse_mode=telegram.ParseMode.MARKDOWN)


def daily_image(context: telegram.ext.CallbackContext):
    try:
        os.chdir("static/img/motivation")
    except FileNotFoundError:
        pass
    images = os.listdir()
    random_image = random.choice(images)
    context.bot.send_photo(GROUP_CHAT_ID, photo=open(random_image, 'rb'))
    os.chdir("../../..")

