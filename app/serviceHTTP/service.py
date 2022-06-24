from django_filters import FilterSet, NumberFilter, CharFilter
from django.db.models import Q
from datetime import datetime

from .models import Shop


class TimeFilter(FilterSet):
    """Фильтр для вывода открытых/закрытых магазинов"""
    city = CharFilter(field_name='city__title')
    street = CharFilter(field_name='street__title')
    opened = NumberFilter(method='open_or_close')

    class Meta:
        model = Shop
        fields = ['city', 'street', 'opened']

    def open_or_close(self, queryset, name, obj):
        now = datetime.now().time()
        if int(obj) == 0:
            response = queryset.filter(Q(open_time__gte=now) | Q(close_time__lte=now))
        if int(obj) == 1:
            response = queryset.filter(open_time__lte=now, close_time__gte=now)
        return response