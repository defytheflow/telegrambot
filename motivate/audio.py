import os
import random

import telegram

from decorators import send_action


@send_action(telegram.ChatAction.UPLOAD_AUDIO)
def audio(update, context):
    try:
        os.chdir("static/sound")
    except FileNotFoundError:
        pass
    audios = os.listdir()
    random_audio = random.choice(audios)
    # reply_markup = telegram.ReplyKeyboardRemove(selective=True)
    context.bot.send_audio(update.message.chat_id, audio=open(random_audio, 'rb'))
    os.chdir("../..")


