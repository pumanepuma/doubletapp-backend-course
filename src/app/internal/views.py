from .models.telegram_user import TelegramUser
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def me(request,user_id):
    user = TelegramUser.objects.filter(user_id=user_id)
    if(user.exists()):
        user=user.first()
        return HttpResponse(f'id: {user_id}, username: {user.username}, phone_number:{user.phone_number}')
    else: 
        return HttpResponseNotFound()
