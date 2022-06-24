from django.urls import path

from .import views


urlpatterns = [
    path('city/', views.CityListView.as_view(), name='city'),
    path('city/<int:pk>/street/', views.CityStreetView.as_view(), name='city_street'),
    path('create_shop/', views.CreateShopView.as_view(), name='create_shop'),
    path('shop/', views.ShopListView.as_view(), name='shop')
]
