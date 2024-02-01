from django.db import models

class ShopList(models.Model):
    name = models.CharField('Название', max_length=100)
    category = models.TextField('Категория')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Названия"
