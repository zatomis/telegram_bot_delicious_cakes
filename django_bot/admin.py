# Register your models here.
from django.contrib import admin
from .models import TelegramUser


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'user', 'id']


admin.site.register(TelegramUser, TelegramUserAdmin)