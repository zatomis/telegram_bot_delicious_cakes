from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from django_bot.models import Cakes

btnMain  = KeyboardButton('📰 Главное меню')
btnMainTechSupport  = KeyboardButton('💻⌨️ Тех.поддержка')
supportUserMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMainTechSupport)
supportUserMenu.add(btnMain)


# --- Menu для всех начальное ---
btnReadyCake   = KeyboardButton('Готовые торты 🍰')
btnConstructCake  = KeyboardButton('Конструктор тортов 🏗')
btnMySettings  = KeyboardButton('Мои настройки ⚙️')
btnFoodBasket  = KeyboardButton('Корзина ')
btnAbout      = KeyboardButton('О нас ...')
main_menu     = ReplyKeyboardMarkup(resize_keyboard = True).add(btnReadyCake)
main_menu.add(btnConstructCake)
main_menu.add(btnMySettings)
main_menu.add(btnFoodBasket)
main_menu.add(btnAbout)
# main_menu.add(btnStartAgain)

# --- Menu Eat ---
btnMenuEatFruit     = KeyboardButton('Фрукты 🍏')
btnMenuEatSFruit    = KeyboardButton('Сухофрукты 🍎')
btnMenuEatYagoda    = KeyboardButton('Ягоды 🫐')
btnMenuEatOreh      = KeyboardButton('Орехи 🥜')
btnMenuEatBot = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMenuEatFruit,btnMenuEatSFruit)
btnMenuEatBot.add(btnMenuEatYagoda)
btnMenuEatBot.add(btnMenuEatOreh)
btnMenuEatBot.add(btnMain)


ReadyCakeRoot = ReplyKeyboardMarkup(resize_keyboard = True)
all_cakes = Cakes.objects.all()
for cake in all_cakes:
    ReadyCakeRoot.add("№" + str(cake.id) + " " +cake.short_title) #символ номер № - это признак для отлова сообщения
ReadyCakeRoot.add(btnMain)

btnReadyCakeVanilaDream = KeyboardButton('Ванильная мечта')
btnReadyCakeVanilaM     = KeyboardButton('Ванилька-манилька')
btnReadyCakeVanilaLady  = KeyboardButton('Леди Ваниль')
ReadyCakeVanila  = ReplyKeyboardMarkup(resize_keyboard = True).add(btnReadyCakeVanilaDream)
ReadyCakeVanila.add(btnReadyCakeVanilaM)
ReadyCakeVanila.add(btnReadyCakeVanilaLady)
ReadyCakeVanila.add(btnMain, btnReadyCake)


btnMenuYesOrNo = ReplyKeyboardMarkup(resize_keyboard = True)
btnMenuYesOrNo.add("Добавить")
btnMenuYesOrNo.add("Не добавлять")
btnMenuYesOrNo.add(btnMain)

btnBasketView  = KeyboardButton('Посмотреть корзину')
btnBasketClear = KeyboardButton('Очистить корзину')
btnBasketOrder = KeyboardButton('Оформить заказ')
btnMenuBasket = ReplyKeyboardMarkup(resize_keyboard = True).add(btnBasketView)
btnMenuBasket.add(btnBasketClear)
btnMenuBasket.add(btnBasketOrder)
btnMenuBasket.add(btnMain)

# btnBReadyCakeVanilaDream = KeyboardButton('Ванильная мечта')
# btnReadyCakeVanilaM     = KeyboardButton('Ванилька-манилька')
# btnReadyCakeVanilaLady  = KeyboardButton('Леди Ваниль')
# btnMenuBasketMenu  = ReplyKeyboardMarkup(resize_keyboard = True).add(btnReadyCakeVanilaDream)
# btnMenuReadyCakeVanila.add(btnReadyCakeVanilaM)
# btnMenuReadyCakeVanila.add(btnReadyCakeVanilaLady)
# btnMenuReadyCakeVanila.add(btnMain)


