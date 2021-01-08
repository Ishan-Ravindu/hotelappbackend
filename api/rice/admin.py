from django.contrib import admin
from .models import Rice, Curry


class curry(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price",
                    "is_stock_avalable")


admin.site.register(Curry, curry)


class rice(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price",
                    "is_stock_avalable")


admin.site.register(Rice, rice)
