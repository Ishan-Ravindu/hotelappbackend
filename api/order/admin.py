from django.contrib import admin
from .models import Order


class Filter(admin.ModelAdmin):
    list_display = ("id", "name", "phone_no", "orders",
                    "total", "adress", "created_at", "updated_at", "status")
    list_filter = ("status", "created_at")


admin.site.register(Order, Filter)
