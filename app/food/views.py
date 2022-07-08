from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FoodListSerializer
from .models import Food, FoodCategory
from django.db.models import Prefetch

class FoodListApiView(APIView):

    def get(self, *args, **kwargs):
        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        ).distinct()
        serializer = FoodListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)