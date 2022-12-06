from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r"workers", WorkerViewSet, basename="workers")
router.register(r"positions", PositionViewSet, basename="positions")

urlpatterns = [
    path('', include(router.urls)),  # get post, с ключем put,delete,get
]
