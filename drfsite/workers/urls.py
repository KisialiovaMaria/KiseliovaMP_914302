from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r"worker", WorkerViewSet, basename="worker")
router.register(r"position", PositionViewSet, basename="position")

urlpatterns = [
    path('', include(router.urls)),  # get post, с ключем put,delete,get
]
