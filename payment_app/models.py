from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=155, verbose_name='maxsulot nomi')
    description = models.TextField(verbose_name='tasnifi')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='narxi')

    class Meta:
        ordering = ['name']
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'

    def __str__(self):
        return self.name
