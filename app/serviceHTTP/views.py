from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from serviceHTTP import serializers
from .models import City, Street, Shop
from .mixin import ErrorMixin
from .service import TimeFilter


class CityListView(ErrorMixin, generics.ListAPIView):
    """Получение всех городов из базы"""
    serializer_class = serializers.CityListSerializers
    queryset = City.objects.all()

    
class CityStreetView(ErrorMixin, generics.ListAPIView):
    """Получение всех улиц города"""
    serializer_class = serializers.CityStreetSerializers

    def get_queryset(self):
        return Street.objects.filter(city_id=self.kwargs['pk'])


class CreateShopView(generics.CreateAPIView):
    """Создание магазина"""
    serializer_class = serializers.CreateShopSerializers
    queryset = Shop.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                return Response({'id': obj.id, 'status': status.HTTP_200_OK})
        except Exception:                
            return Response(status.HTTP_400_BAD_REQUEST)


class ShopListView(ErrorMixin, generics.ListAPIView):
    """Вывод списка всех магазинов"""
    queryset = Shop.objects.all()
    serializer_class = serializers.ShopListSerializers
    filterset_class = TimeFilter
    lookup_field = 'slug'
    
