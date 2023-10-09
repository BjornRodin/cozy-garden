from django.contrib import admin
from .models import Flowers, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'color',
        'sku',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Flowers, ProductAdmin)
admin.site.register(Category, CategoryAdmin)