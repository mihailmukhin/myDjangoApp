from django.db import models


class Recipes(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    photo = models.CharField('Картинка', max_length=150)
    composition = models.TextField('Состав')
    method = models.TextField('Способ приготовления')

    def __str__(self):
        return self.name
