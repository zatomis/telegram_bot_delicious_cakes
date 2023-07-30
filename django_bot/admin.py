# Register your models here.
from django.contrib import admin
from .models import (
    TelegramUser,
    Cakes,
    Ingredients,
    Images,
    Orders,
    Constructor,
    Cart)


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'name', 'phone']


@admin.register(Cakes)
class CakesAdmin(admin.ModelAdmin):
    list_display = ['short_title', 'price']



@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['title', 'units', 'count', 'price']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'status', 'all_price']

@admin.register(Constructor)
class ConstructorAdmin(admin.ModelAdmin):
    list_display = ['title', 'levels_number', 'levels_shape']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'product', 'created_at']


admin.site.register(Images)
