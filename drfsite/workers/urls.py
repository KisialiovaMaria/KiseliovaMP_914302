from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r"workers", WorkerViewSet, basename="workers")
router.register(r"control-points", ControlPointViewSet, basename="control-points")
router.register(r"notifications", NotificationsViewSet, basename="notifications")
router.register(r"control-list", ControlListViewSet, basename="control-list")



urlpatterns = [
    path('', include(router.urls)),  # get post, с ключем put,delete,get
    path('positions/', PositionAPIView.as_view()),
    path('departments/', DepartmentAPIView.as_view()),
    path('visit-juornal/', VisitJuornalAPIView.as_view()),
    path('send-type/', SendTypeAPIView.as_view()),
    path('event-type/', EventTypeAPIView.as_view()),
    path('workers/updateImage/<int:pk>/', WorkerPostAPIView.as_view()),
    path('control-list-of-worker/<int:pk>/', ControlListAPIViewByID.as_view()),
    #path('control-points/', ControlPointAPIView.as_view()),
   # path('control-points/camera/<id>', ControlPointUpdateCameraActivityView.as_view()),
    path('face-recognition/start/', FaceRecognitionStart),
    path('face-recognition/stop/', FaceRecognitionStop),
   # path('video-presentation/', VideoPresentation),
]
