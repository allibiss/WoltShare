from django.contrib import admin

from .models import CustomUser, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        # "seller",
        "quantity",
        "price_per_quant",
        "description",
        "food_type",
        "packaging",
        "image",
        "ingredients",
        "date",
        "title",
    )


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "username",
        "name",
        "phone",
        "lat",
        "lon",
        "address",
    )
