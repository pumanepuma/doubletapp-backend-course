import os
import django
#разрешаем работу с базой данных в асинхронных методах
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

import logging

from app.internal.models.telegram_user import TelegramUser
from django.core.management import BaseCommand

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton
from telegram.ext import (
    ContextTypes,
)

SET_PHONE = 1

#команда для старта и записи нового юзера
async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    TelegramUser.objects.get_or_create(user_id=user_id, username=username)
    await update.message.reply_text(f'hey, {username}')

#запрос номера телефона
async def get_phone(update:Update, context:ContextTypes.DEFAULT_TYPE) -> int:
    con_key = KeyboardButton('share contact',request_contact=True)
    keyboard_markup = [[con_key]]
    await update.message.reply_text(
        'would you share your contact info?',
        reply_markup=ReplyKeyboardMarkup(keyboard_markup)
    )
    return SET_PHONE

#запись номера телефона в базу
async def set_phone(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    phone_number = update.message.contact.phone_number
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    user = TelegramUser.objects.filter(user_id=user_id)
    if(user.exists()):
        user = user.first()
        setattr(user,'phone_number',phone_number)
        user.save()
    else:
        TelegramUser.objects.create(username=username,user_id=user_id, phone=phone_number)
    await update.message.reply_text('contact information has been updated',
    reply_markup=ReplyKeyboardRemove())

#отображение информации о юзере
async def me(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user = TelegramUser.objects.get(user_id=user_id)
    #если номер не записан, команда недоступна
    if(user.phone_number):
        await update.message.reply_text(f'id: {user.user_id}, username: {user.username}, phone:{user.phone_number}')
    else:
        await update.message.reply_text('please, fill your contact information via /set_phone command')

