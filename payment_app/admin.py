from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price']


admin.register(Product, ProductAdmin)