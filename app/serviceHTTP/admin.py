from django.contrib import admin

from .models import City, Shop, Street


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city')