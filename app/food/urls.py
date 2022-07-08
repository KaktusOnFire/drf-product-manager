from django.urls import path
from .views import FoodListApiView

urlpatterns = [
    path('v1/foods', FoodListApiView.as_view(), name="foods"),
]