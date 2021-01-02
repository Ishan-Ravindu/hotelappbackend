from django.contrib import admin
from .models import Order


class Filter(admin.ModelAdmin):
    list_display = ("id", "name", "phone_no", "orders",
                    "total", "adress", "created_at", "updated_at", "status")
    list_filter = ("status", "created_at")
    actions = ("set_status_to_conform", "set_status_to_diliver",
               "set_status_to_rejected")
    search_fields = ("name", "phone_no", "adress")

    def set_status_to_conform(self, request, queryset):
        count = queryset.update(status="conform")
        self.message_user(
            request, "{} filds are changed status to conform".format(count))

    def set_status_to_diliver(self, request, queryset):
        count = queryset.update(status="dileved")
        self.message_user(
            request, "{} filds are changed status to dileved".format(count))

    def set_status_to_rejected(self, request, queryset):
        count = queryset.update(status="rejected")
        self.message_user(
            request, "{} filds are changed status to rejected".format(count))


admin.site.register(Order, Filter)
