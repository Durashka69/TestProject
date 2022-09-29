from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,20}$', message='+996111222333'
    )
    phone = models.CharField(
        validators=[phone_regex], max_length=30, unique=True
    )


class Category(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название категории'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# class LostLocation(models.Model):
#     title = models.CharField(
#         verbose_name='Название локации',
#         max_length=255, 
#     )
#     lost_item = models.ForeignKey(
#         'LostItem',
#         on_delete=models.
#     )

#     def __str__(self):
#         return self.title


class Item(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название вещи'
    )
    picture = models.ImageField(
        upload_to='images/found_items',
        verbose_name='Изображение найденного предмета',
        null=True, blank=True
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='items'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    geotag = models.CharField(
        max_length=255, verbose_name='Место потери'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True, blank=True
    )
    pickup_location = models.CharField(
        max_length=255, 
        verbose_name='Локация для передачи',
        null=True, blank=True
    )
    is_lost = models.BooleanField(
        default = False,
        verbose_name = 'Является ли вещь потерянной'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Найденная вещь'
        verbose_name_plural = 'Найденные вещи'


# class LostItem(models.Model):
#     title = models.CharField(
#         max_length=255, verbose_name='Название предмета'
#     )
#     category = models.ForeignKey(
#         Category, 
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True
#     )
#     picture = models.ImageField(
#         upload_to='images/lost_items',
#         verbose_name='Изображение потерянного предмета',
#         null=True, blank=True
#     )
#     location1 = models.URLField(
#         max_length=255, 
#         verbose_name='Первая локация'
#     )
#     location2 = models.URLField(
#         max_length=255, 
#         verbose_name='Вторая локация',
#         null=True, blank=True
#     )
#     location3 = models.URLField(
#         max_length=255, 
#         verbose_name='Третья локация',
#         null=True, blank=True
#     )
    
#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = 'Потерянная вещь'
#         verbose_name_plural = 'Потерянные вещи'
