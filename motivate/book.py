import telegram.ext

from decorators import send_action


@send_action(telegram.ChatAction.UPLOAD_DOCUMENT)
def book(update, context):
    # reply_markup = telegram.ReplyKeyboardRemove(selective=True)
    context.bot.send_document(update.message.chat_id, document=open("data/pdf/walter-isaacson.pdf", "rb"))