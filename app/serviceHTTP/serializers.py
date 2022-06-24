from rest_framework import serializers

from .models import City, Street, Shop


class CityListSerializers(serializers.ModelSerializer):
    """Получение всех городов из базы"""
    class Meta:
        model = City
        fields = '__all__'


class CityStreetSerializers(serializers.ModelSerializer):
    """Получение всех улиц города"""
    class Meta:
        model = Street
        fields = '__all__'


class CreateShopSerializers(serializers.ModelSerializer):
    """Создание магазина"""
    class Meta:
        model = Shop
        fields = '__all__'


class ShopListSerializers(serializers.ModelSerializer):
    """Вывод списка всех магазинов"""
    city = serializers.ReadOnlyField(source='city.title')
    street = serializers.ReadOnlyField(source='street.title')

    class Meta:
        model = Shop
        fields = '__all__'


