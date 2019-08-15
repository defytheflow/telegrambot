"""This is the main file that starts the bot."""

import logging
import datetime

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

from admin.handlers import speak, todo

from menu.menu import menu

from motivate.motivate import motivate
from motivate.quote import quote
from motivate.image import image
from motivate.audio import audio
from motivate.book import book

from learn.learn import learn, fact

from entertain.entertain import entertain, party

from handlers import start, me, unknown
from callbacks import type_command_callback
from jobs import wake_up, daily_quote, daily_image, daily_fact

from settings import TOKEN


class TelegramBot:

    def __init__(self, token):
        self.token = token
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.job = self.updater.job_queue

    def add_handlers(self, *handlers):
        for handler in handlers:
            self.dispatcher.add_handler(handler)

    def init_admin_handlers(self):
        """ Here we initialize all the admin commands. """
        speak_handler = CommandHandler("speak", speak)
        todo_handler = CommandHandler("todo", todo)
        self.add_handlers(speak_handler, todo_handler)

    def init_menu_handlers(self):
        """ Here we initialize all the commands from 'menu' module. """
        menu_handler = CommandHandler("menu", menu)
        self.add_handlers(menu_handler)

    def init_motivate_handlers(self):
        """ Here we initialize all the commands from 'motivate' module. """
        motivate_handler = CommandHandler("motivate", motivate)
        quote_handler = CommandHandler("quote", quote)
        image_handler = CommandHandler("image", image)
        audio_handler = CommandHandler("audio", audio)
        book_handler = CommandHandler("book", book)
        self.add_handlers(motivate_handler,
                          quote_handler, image_handler,
                          audio_handler, book_handler)

    def init_learn_handlers(self):
        """ Here we initialize all the commands from 'learn' module. """
        learn_handler = CommandHandler("learn", learn)
        fact_handler = CommandHandler("fact", fact)
        self.add_handlers(learn_handler, fact_handler)

    def init_entertain_handlers(self):
        """ Here we initialize all the commands from 'entertain' module. """
        entertain_handler = CommandHandler("entertain", entertain)
        party_handler = CommandHandler("party", party)
        self.add_handlers(entertain_handler, party_handler)

    def init_handlers(self):
        """ Here we initialize basic bot commands. """
        start_handler = CommandHandler("start", start)
        me_handler = CommandHandler("me", me)
        unknown_handler = MessageHandler(Filters.command, unknown)
        self.add_handlers(start_handler, me_handler,
                          unknown_handler)

    def init_callbacks(self):
        type_command_handler = CallbackQueryHandler(type_command_callback)
        self.add_handlers(type_command_handler)

    def init_jobs(self):
        """ Here we initialize commands that run repeatedly at a specific rate. """
        # self.job.run_once(wake_up, 0)
        self.job.run_daily(daily_quote, time=datetime.time(6, 0))  # todo Time on servers is falls behind 3 hours
        self.job.run_daily(daily_image, time=datetime.time(7, 0))
        self.job.run_daily(daily_fact, time=datetime.time(8, 0))
        self.job.run_daily(daily_quote, time=datetime.time(18, 0))
        self.job.run_daily(daily_image, time=datetime.time(19, 0))
        self.job.run_daily(daily_fact, time=datetime.time(20, 0))

    def run(self):
        self.updater.start_polling()
        self.updater.idle()


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)


if __name__ == "__main__":
    steve = TelegramBot(TOKEN)
    steve.init_admin_handlers()
    steve.init_menu_handlers()

    steve.init_motivate_handlers()
    steve.init_learn_handlers()
    steve.init_entertain_handlers()

    steve.init_handlers()
    steve.init_callbacks()
    steve.init_jobs()

    steve.run()
