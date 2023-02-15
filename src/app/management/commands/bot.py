from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from app.internal.models.telegram_user import TelegramUser
from app.internal.transport.bot import handlers
from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
 
class Command(BaseCommand):
    def handle(self, *args, **options):
        load_dotenv()
        application = Application.builder().token(os.environ.get('TOKEN')).build()

        #привязваем к боту созданные команды
        application.add_handler(ConversationHandler(
            entry_points=[
                CommandHandler('start',handlers.start_command),
                CommandHandler('set_phone',handlers.get_phone),
                CommandHandler('me',handlers.me)
            ],
            states={
                handlers.SET_PHONE: [MessageHandler(filters.CONTACT,handlers.set_phone)]
            },
            fallbacks=[
                CommandHandler('set_phone',handlers.get_phone),
                CommandHandler('me',handlers.me)
            ]
        ))

        # Run the bot until the user presses Ctrl-C
        application.run_polling()