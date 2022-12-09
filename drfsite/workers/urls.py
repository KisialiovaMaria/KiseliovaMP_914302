from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r"workers", WorkerViewSet, basename="workers")
router.register(r"control-points", ControlPointViewSet, basename="control-points")
router.register(r"notifications", ControlPointViewSet, basename="notifications")


urlpatterns = [
    path('', include(router.urls)),  # get post, с ключем put,delete,get
    path('positions/', PositionAPIView.as_view()),
    path('departments/', DepartmentAPIView.as_view()),
    path('visit-juornal/', VisitJuornalAPIView.as_view()),
    path('send-type/', SendTypeAPIView.as_view()),
    path('event-type/', EventTypeAPIView.as_view()),
    #path('face-recognition', FaceRecognition),
    path('video-presentation', VideoPresentation)
]
