import telegram.ext

from decorators import send_action


@send_action(telegram.ChatAction.TYPING)
def menu(update, context):
    me_button = telegram.InlineKeyboardButton(text="/me", callback_data="me")
    motivate_button = telegram.InlineKeyboardButton(text="/motivate", callback_data="motivate")
    learn_button = telegram.InlineKeyboardButton(text="/learn", callback_data="learn")
    entertain_button = telegram.InlineKeyboardButton(text="/entertain", callback_data="entertain")
    keyboard = [[me_button],
                [learn_button, motivate_button, entertain_button]]
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(update.message.chat_id, photo=open("static/img/photo/menu-steve.jpg", "rb"))
    context.bot.send_message(update.message.chat_id, text="Here is the menu of my commands.", reply_markup=reply_markup)


