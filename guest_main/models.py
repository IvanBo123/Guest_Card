from django.db import models
from .models import *


# Create your models here.
class About_usInfo(models.Model):
    description = models.TextField(max_length=500, verbose_name="Описание")
    image = models.ImageField(
        upload_to='guest_card_img/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class StatisticInfo(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование статуса")
    href = models.CharField(max_length=50, verbose_name="Ссылка на иконку")
    value = models.IntegerField(verbose_name="Количество")
    cent = models.CharField(max_length=3, blank=True,
                            null=True, verbose_name="Единица измерения")

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'


class Type_ofCompanions(models.Model):
    types = models.CharField(max_length=100, verbose_name="Тип заведения")
    tag = models.CharField(max_length=100, verbose_name="html-тэг")

    class Meta:
        verbose_name = 'Тип заведения'
        verbose_name_plural = 'Типы заведений'

    def __str__(self):
        return f'{self.types}'


class Companions(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование заведения")
    status = models.FloatField(blank=True,
                               null=True, verbose_name="Статус заведения")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    image = models.ImageField(
        upload_to='guest_card_img/', blank=True, null=True, verbose_name="Фотография")
    type_of = models.ForeignKey(
        Type_ofCompanions, on_delete=models.CASCADE, verbose_name="Тип заведения")
    href = models.CharField(max_length=500, blank=True,
                            null=True, verbose_name="Ссылка")

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'
        ordering = ['type_of', ]

    def __str__(self):
        return f'{self.name}'


class Social_Hubs(models.Model):
    icon = models.CharField(max_length=50, verbose_name="Ссылка на иконку")
    href = models.CharField(max_length=500, blank=True, null=True, verbose_name="Ссылка")

    class Meta:
        verbose_name = 'Соц. сеть'
        verbose_name_plural = 'Соц. сети'
