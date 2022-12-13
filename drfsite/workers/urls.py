from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *

router = routers.SimpleRouter()
router.register(r"workers", WorkerViewSet, basename="workers")
router.register(r"control-points", ControlPointViewSet, basename="control-points")
router.register(r"notifications", NotificationsViewSet, basename="notifications")
router.register(r"control-points-whole", ControlPointWholeViewSet, basename="control-points-whole")



urlpatterns = [
    path('', include(router.urls)),  # get post, с ключем put,delete,get
    path('positions/', PositionAPIView.as_view()),
    path('departments/', DepartmentAPIView.as_view()),
    path('visit-juornal/', VisitJuornalAPIView.as_view()),
    path('visit-juornal-whole/', VisitJuornalWholeAPIView.as_view()),
    path('send-type/', SendTypeAPIView.as_view()),
    path('visit-type/', VisitTypeAPIView.as_view()),
    path('event-type/', EventTypeAPIView.as_view()),
    path('workers/updateImage/<int:pk>/', WorkerPutAPIView.as_view()),
    #path('control-points-whole/',ControlPointWholeAPIView.as_view()),
    #path('control-list-of-point/<int:pk>/', ControlListAPIViewByID.as_view()),
    #path('control-points/', ControlPointAPIView.as_view()),
   # path('control-points/camera/<id>', ControlPointUpdateCameraActivityView.as_view()),
    path('face-recognition/start/<int:pk>/', FaceRecognitionStart),
    path('face-recognition/stop/<int:pk>/', FaceRecognitionStop),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
   # path('video-presentation/', VideoPresentation),
]
