
from datetime import date
from django.db import models


# class TelegramUser(models.Model):
#     user = models.OneToOneField(
#         to=get_user_model(),
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#         related_name='telegram_user'
#     )
class TelegramUser(models.Model):
    chat_id = models.CharField(
        max_length=20,
        verbose_name="Телеграмм id"
    )

    name = models.CharField(
        max_length=30,
        default="",
        verbose_name="Имя клиента"
        )
    phone = models.CharField(
        max_length=30,
        default="",
        verbose_name="Номер клиента"
        )

    def get_id(self):
        return self.id

    def __str__(self) -> str:
        return f'{self.name}. {self.chat_id}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Cakes(models.Model):
    image_id = models.ForeignKey('Images', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    short_title = models.CharField(max_length=30) 
    description = models.TextField()

    def __str__(self):
        return f'{self.short_title} {self.price}'

    class Meta:
        verbose_name = "Торт"
        verbose_name_plural = "Список тортов"


class Images(models.Model):
    alt = models.CharField(max_length=50)
    path = models.ImageField(upload_to="images/")

    def __str__(self):
        return f'{self.alt}'
    
    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"


class Ingredients(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название"
        )
    units = models.CharField(
        max_length=30,
        verbose_name="Единица измерения")
    count = models.IntegerField(
        default=1,
        verbose_name="Количество",
    )
    price = models.IntegerField(
        default=1,
        verbose_name="Цена",
    )
    
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"


class Constructor(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3

    LEVELS_NUMBER_CHOICES = [
        (ONE, 1),
        (TWO, 2),
        (THREE, 3)
    ]

    CIRCLE = "Круг"
    SQUARE = "Квадрат"
    RECTANGLE = "Прямоугольник"

    LEVELS_SHAPE_CHOICES = [
        (CIRCLE, "Круг"),
        (SQUARE, "Квадрат"),
        (RECTANGLE, "Прямоугольник")
    ]

    title = models.CharField(
        max_length=30,
        default="",
        verbose_name="Название торта")

    levels_number = models.IntegerField(
        choices=LEVELS_NUMBER_CHOICES,
        default=ONE,
        verbose_name="Количество уровней"
        )
    levels_shape = models.CharField(
        max_length=30,
        choices=LEVELS_SHAPE_CHOICES,
        default=CIRCLE,
        verbose_name="Форма уровней"
        )
    
    ingredients_id = models.ManyToManyField(
        Ingredients,
        verbose_name="Ингридиенты")

    cake_writing = models.CharField(
        max_length=250,
        default="",
        blank=True,
        verbose_name="Надпись на торте"
        )
   
    
    def get_price(self):
        all_price = self.levels_number * 200

        if self.cake_writing:
            all_price += 150
        
        ingredients = self.ingredients_id.all()

        for ingredient in ingredients:
            all_price += ingredient.price

        return all_price

    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Конструктор"
        verbose_name_plural = "Торты-конструкторы"


class Orders(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3

    STATUS_CHOICES = [
        (ONE, "Принят"),
        (TWO, "Готовиться"),
        (THREE, "Доставка")
    ]

    client_id = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        verbose_name="Клиент"
        )
    execution_date = models.DateField(
        default=date.today,
        verbose_name="Дата исполнения",
        )
    
    cake_id = models.ManyToManyField(
        Cakes,
        verbose_name="Готовые торты")
    constructor_cake_id = models.ManyToManyField(
        Constructor,
        verbose_name="Сконструированные торты"
        )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        verbose_name="Статус заказа",
    )
    comment = models.TextField(
        max_length=300,
        default=""
    )

    delivery_address = models.CharField(
        max_length=250,
        blank=False, 
        default="",
        verbose_name="Адрес доставки"
        )
    
    all_price = models.IntegerField(
        default=0,
        verbose_name="Общая стоимость"
    )
    
    def __str__(self):
        return f'{self.client_id.name}, {self.delivery_address}'
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    

class Cart(models.Model):
    client_id = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        verbose_name="Клиент"
        )

    product = models.ForeignKey(
        Cakes,
        on_delete=models.CASCADE,
        verbose_name="Торт"
        )

    created_at = models.DateTimeField(
        verbose_name="Время добавления в корзину",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Заказы клиентов в корзинах"




    

