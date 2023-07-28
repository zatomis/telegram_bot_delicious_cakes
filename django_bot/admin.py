# Register your models here.
from django.contrib import admin
from .models import TelegramUser, Catalog


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'id']


admin.site.register(TelegramUser)
admin.site.register(Catalog)