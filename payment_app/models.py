from django.db import models
from django.template.defaultfilters import slugify


def get_image_filename(instance, filename):
    name = instance.name
    slug = slugify(name)
    return f"products/{slug}-{filename}"


class Product(models.Model):
    name = models.CharField(max_length=155, verbose_name='maxsulot nomi')
    desc = models.TextField(verbose_name='tasnifi')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='narxi')
    thumbnail = models.ImageField(upload_to=get_image_filename, blank=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'

    def __str__(self):
        return self.name
