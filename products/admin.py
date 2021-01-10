from django.contrib import admin
from .models import Product, Category, Color
"""
Register Product, Categiory and Color models
Customize fields being displayed in admin view
"""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = (
        'product_code',
        'avg_rating',
    )
    fields = (
        'name',
        'description',
        'category',
        'price',
        'many_colors',
        'color',
        'main_pic',
        'pic2',
        'pic3',
        'pic4',
        'release_date'
    )
    list_display = (
        'name',
        'category',
        'price',
        'added_date',
        'release_date',
    )
    ordering = ('product_code',)
    date_hierarchy = 'added_date'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color_hex',
    )
