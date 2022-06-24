from rest_framework.response import Response
from rest_framework import status


class ErrorMixin:
    """Миксин для обработки ошибок, при успехе возвращать 200, при ошибке 400 соответственно"""
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response({'status': status.HTTP_200_OK ,'response': serializer.data})
        except Exception:
            return Response(status.HTTP_400_BAD_REQUEST)