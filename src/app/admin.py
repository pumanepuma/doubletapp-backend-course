from django.contrib import admin

from app.internal.admin.admin_user import AdminUserAdmin

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"

from app.internal.models.telegram_user import TelegramUser

#Добавляем модель юзера в админку
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username','phone_number','user_id')

admin.site.register(TelegramUser,TelegramUserAdmin)