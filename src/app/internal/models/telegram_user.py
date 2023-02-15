from django.db import models

class TelegramUser(models.Model):
    user_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100, blank=True, default='')
    phone_number = models.CharField(max_length=16,blank=True,default='')
