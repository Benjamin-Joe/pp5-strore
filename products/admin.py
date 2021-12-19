from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )


class CaregoryAdmin(admin.ModelAdmin):
    name = 'name',

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CaregoryAdmin)

