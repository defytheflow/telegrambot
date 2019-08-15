import telegram.ext

from decorators import send_action


@send_action(telegram.ChatAction.TYPING)
def motivate(update, context):
    """
        This function displays all the available commands for 'motivate' module.
        It has got only informational purpose, no functionality.
    """
    keyboard = [["/quote", "/image"],
                ["/audio", "/book"]]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True,
                                                one_time_keyboard=True, selective=True)
    text = "I have a lot of motivational stuff for you, what would you like?"
    context.bot.send_photo(update.message.chat_id, photo=open("static/img/photo/motivate-steve.jpg", "rb"))
    context.bot.send_message(update.message.chat_id, text=text, reply_markup=reply_markup)

