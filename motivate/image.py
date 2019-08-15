import os
import random

import telegram

from decorators import send_action


@send_action(telegram.ChatAction.UPLOAD_PHOTO)
def image(update, context):
    try:
        os.chdir("static/img/motivation")
    except FileNotFoundError:
        pass
    images = os.listdir()
    random_image = random.choice(images)
    # reply_markup = telegram.ReplyKeyboardRemove(selective=True)
    context.bot.send_photo(update.message.chat_id, photo=open(random_image, 'rb'))
    os.chdir("../../..")


