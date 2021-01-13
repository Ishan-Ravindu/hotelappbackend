from django.contrib import admin
from .models import Rice, Curry


class curry(admin.ModelAdmin):
    list_display = ("id", "name", "price",
                    "is_stock_avalable")

    list_filter = ("is_stock_avalable",)
    search_fields = ("name",)
    actions = ("stock_avalable", "stock_not_avalable", "delete_selected")

    def stock_avalable(self, request, queryset):
        count = queryset.update(is_stock_avalable=True)
        self.message_user(
            request, "{} filds are changed to stock avalable ".format(count))

    def stock_not_avalable(self, request, queryset):
        count = queryset.update(is_stock_avalable=False)
        self.message_user(
            request, "{} filds are changed to stock not avalable ".format(count))


admin.site.register(Curry, curry)


class rice(admin.ModelAdmin):
    list_display = ("id", "name", "price",
                    "is_stock_avalable")

    list_filter = ("is_stock_avalable", )
    search_fields = ("name",)
    actions = ("stock_avalable", "stock_not_avalable", "delete_selected")

    def stock_avalable(self, request, queryset):
        count = queryset.update(is_stock_avalable=True)
        self.message_user(
            request, "{} filds are changed to stock avalable ".format(count))

    def stock_not_avalable(self, request, queryset):
        count = queryset.update(is_stock_avalable=False)
        self.message_user(
            request, "{} filds are changed to stock not avalable ".format(count))


admin.site.register(Rice, rice)
