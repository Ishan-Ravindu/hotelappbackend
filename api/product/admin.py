from django.contrib import admin
from .models import Product


class Filter(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price",
                    "is_stock_avalable")
    list_filter = ("is_stock_avalable", "category")


admin.site.register(Product, Filter)
