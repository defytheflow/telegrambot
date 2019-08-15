""" This module has all the callbacks that are used in entire program. """

import telegram.ext


def type_command_callback(update, context):
    """
        This function informs the user that he needs to type the command,
        not just press the button on the inline keyboard.
    """
    callback_data = update.callback_query.data
    # chat_id = update.callback_query["message"]["chat"]["id"]  #todo might be useful
    context.bot.answer_callback_query(update.callback_query.id, text=f"Please type /{callback_data} .", show_alert=True)


