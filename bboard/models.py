from django.db import models as modelsClass
from django.views.generic.list import ListView


class Rubric(modelsClass.Model):

    name = modelsClass.CharField(max_length=30, db_index=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Участки'
        verbose_name = 'Участок'
        ordering = ['name']


class masters(modelsClass.Model):

    UserLogin = modelsClass.CharField(max_length=40, unique=False, verbose_name='ФИО мастера')
    cardNumber = modelsClass.BigIntegerField(primary_key=True, null=False, blank=False, editable= True, unique=False, verbose_name='Номер Карты')
    accessLevel = modelsClass.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Уровень доступа')
    published = modelsClass.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    rubric = modelsClass.ForeignKey('Rubric', null=True,
                               on_delete=modelsClass.PROTECT, verbose_name='Участок')


    def __str__(self):
        return self.UserLogin



    class Meta:
        verbose_name_plural = 'Список Мастеров'
        ordering = ['published']



