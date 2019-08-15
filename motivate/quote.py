import json
import random

import telegram

from decorators import send_action


@send_action(telegram.ChatAction.TYPING)
def quote(update, context):
    with open("data/json/quotes.json", "r", encoding="cp1251") as file:
        phy_quotes = json.load(file)
    random_quote = random.choice(phy_quotes)
    quote_text = random_quote["quoteText"]
    quote_author = random_quote["quoteAuthor"]
    # reply_markup = telegram.ReplyKeyboardRemove(selective=True)
    context.bot.send_message(update.message.chat_id, text=f"{quote_text}\n\n*{quote_author}*",
                             parse_mode=telegram.ParseMode.MARKDOWN)

