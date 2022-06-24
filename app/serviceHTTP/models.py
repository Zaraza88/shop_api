from django.db import models


class City(models.Model):
    title = models.CharField('Название города', max_length=50)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Street(models.Model):
    title = models.CharField('Название улицы', max_length=50)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='street_city')

    def __str__(self):
        return f'Улица - {self.title}, {self.city}'

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

class Shop(models.Model):
    title = models.CharField('Название магазина', max_length=50)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='city_shop')
    street = models.ForeignKey(Street, on_delete=models.PROTECT, related_name='shop_street')
    house = models.IntegerField('Номер дома')
    open_time = models.TimeField('Время открытия')
    close_time = models.TimeField('Время закрытия')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'