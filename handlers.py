"""This module has all the 'basic' handlers for the bot. Like 'start', 'updates' and so on. """

import csv

import telegram.ext

from decorators import send_action


@send_action(telegram.ChatAction.TYPING)
def start(update, context):
    user_id = str(update.effective_user["id"])
    user_first_name = update.effective_user["first_name"]
    user_last_name = update.effective_user["last_name"]
    if not user_last_name:
        user_last_name = ""
    user_info = [user_id, user_first_name, user_last_name]
    chat_name = update.effective_chat["title"]
    bot_name = context.bot.first_name

    with open("admin/data/csv/users.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        users = list(reader)

    if user_info not in users:
        with open("admin/data/csv/users.csv", "a", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(user_info)

    if not chat_name:
        reply_text = (f"Hello, *{user_first_name}*.\n"
                      f"My name is *{bot_name}* and I will be *assisting* you on your way to *greatness*.")
    else:
        reply_text = (f"Hello, *{user_first_name}*. Welcome to *{chat_name}*.\n"
                      f"My name is *{bot_name}* and I will be *assisting* you on your way to *greatness*.")

    context.bot.send_animation(update.message.chat_id, animation=open("static/animation/start.gif", "rb"))
    context.bot.send_message(update.message.chat_id, text=reply_text, parse_mode=telegram.ParseMode.MARKDOWN)


@send_action(telegram.ChatAction.TYPING)
def me(update, context):
    """ Bot returns user-info. """
    user_first_name = update.effective_user["first_name"]
    first_name_text =  f"Your first name is *{user_first_name}*.\n"
    user_last_name = update.effective_user["last_name"]
    if user_last_name:
        last_name_text = f"Your last name is *{user_last_name}*.\n"
    else:
        last_name_text = ""
    user_photo_info = context.bot.get_user_profile_photos(user_id=update.effective_user["id"], limit=1)
    if user_photo_info['total_count'] != 0:
        user_photo = user_photo_info['photos'][0][-1]["file_id"]
        photo_text = "Here is what you *look* like."
        context.bot.send_photo(update.message.chat_id, photo=open("static/img/photo/me-steve.jpg", "rb"))
        context.bot.send_message(update.message.chat_id, text=first_name_text + last_name_text + photo_text,
                                 parse_mode=telegram.ParseMode.MARKDOWN)
        context.bot.send_photo(update.message.chat_id, photo=user_photo)
    else:
        context.bot.send_photo(update.message.chat_id, photo=open("static/img/photo/me-steve.jpg", "rb"))
        context.bot.send_message(update.message.chat_id, text=first_name_text + last_name_text,
                                 parse_mode=telegram.ParseMode.MARKDOWN)


@send_action(telegram.ChatAction.TYPING)
def unknown(update, context):
    context.bot.send_message(update.message.chat_id,
                             text="Sorry I didn't understand that command.")

