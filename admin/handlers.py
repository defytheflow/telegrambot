""" This module consists of admin commands. """

import textwrap

import telegram

from decorators import restricted, send_action
from settings import ADMIN_CHAT_ID, GROUP_CHAT_ID


@restricted
@send_action(telegram.ChatAction.TYPING)
def speak(update, context):
    admin_says = " ".join(context.args)
    if admin_says:
        context.bot.send_message(ADMIN_CHAT_ID, text="Done, sir")
        context.bot.send_message(GROUP_CHAT_ID, text=admin_says)
    else:
        return


@restricted
@send_action(telegram.ChatAction.TYPING)
def todo(update, context):
    admin_says = "- " + " ".join(context.args).capitalize()
    task = textwrap.fill(admin_says, 80)

    with open("admin/data/txt/to-do.txt", "a") as file:
        file.write(task + "\n")

    context.bot.send_message(ADMIN_CHAT_ID, text="Done, sir")