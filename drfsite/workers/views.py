import threading
import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action, api_view
from django.views.decorators import gzip
from rest_framework.response import Response

import FR.face_recognition_block
from FR.face_recognition_block import FaceRecognizer
from .models import *
from .Serializers import *


# from rest_framework import viewsets


# APIView

class WorkerViewSet(viewsets.ModelViewSet):  # предоставляет все CRUD
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    # def get_queryset(self):
    #     return Worker.objects.all()[:3]

    # @action(methods=['get'], detail=True) # detail=True для одного False для всех
    # def position(self, request, pk=None):
    #     positions = Position.objects.get(pk=pk)
    #     return Response({'cats':positions.name})


class PositionAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class DepartmentAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SendTypeAPIView(generics.ListAPIView):
    queryset = SendType.objects.all()
    serializer_class = SendTypeSerializer


class EventTypeAPIView(generics.ListAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class VisitJuornalAPIView(generics.ListAPIView):
    queryset = VisitJuornal.objects.all()
    serializer_class = VisitJuornalSerializer


class ControlPointViewSet(viewsets.ModelViewSet):
    queryset = ControlPoint.objects.all()
    serializer_class = ControlPointSerializer


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer


@gzip.gzip_page
def VideoPresentation(reqest):
    try:
        # cam = VideoCamera()

        cam2 = FR.face_recognition_block.FaceRecognizer(['./FR/images/masha.png', './FR/images/obama.png'], ['1', '2'])
        cam2.start_video_representing()
        for _ in range(1000):
            pass
        print('stop')
        cam2.stop_video_representing()
        # gen(cam)
        # cam2.start_recognition()

        return StreamingHttpResponse(FR.face_recognition_block.gen(cam2),
                                     content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        pass
    return render(reqest, 'C:/Users/masha/PycharmProjects/rest_api_workers/drfsite/workers/workers.html')


@gzip.gzip_page
def Home(reqest):
    try:
        # cam = VideoCamera()

        cam2 = FR.face_recognition_block.FaceRecognizer(['./FR/images/masha.png', './FR/images/obama.png'], ['1', '2'])
        cam2.start_video_representing()
        for _ in range(1000):
            pass
        print('stop')
        cam2.stop_video_representing()
        # gen(cam)
        # cam2.start_recognition()

        return StreamingHttpResponse(FR.face_recognition_block.gen(cam2),
                                     content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        pass
    return render(reqest, 'C:/Users/masha/PycharmProjects/rest_api_workers/drfsite/workers/workers.html')

# @api_view(['GET'])
# def fr_view(request):
#     video_capture = cv2.VideoCapture(0)
#     known_face_names = [
#         "Barack Obama",
#         "Masha Kiseliova"
#     ]
#     recogn = FaceRecognizer(video_capture, ['./FR/images/obama.png', './FR/images/masha.png'], known_face_names)
#     recogn.start_recognition()

# class PhotoBaseViewSet(viewsets.ModelViewSet):
#     queryset = PhotoBase.objects.all()
#     serializer_class = PhotoSerializer
#
#

#
# class CameraAPIViewDeleteCreate(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
#     queryset = Camera.objects.all()
#     serializer_class = CameraSerializer
#
#
# class ControlListViewSet(viewsets.ModelViewSet):
#     queryset = ControlList.objects.all()
#     serializer_class = ControlListSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class NotificationsViewSet(viewsets.ModelViewSet):
#     queryset = Notifications.objects.all()
#     serializer_class = NotificationsSerializer
#
#
# class VisitTypeAPIView(generics.ListAPIView):
#     queryset = VisitType.objects.all()
#     serializer_class = VisitTypeSerializer
#
#


# наследуется от класса котрый определяет набор запросов которые можно использовать
# class WorkerAPIList(generics.ListCreateAPIView):
#     queryset = Worker.objects.all() # данные которые будут возвращаться по эапросу
#     serializer_class = WorkerSerializer # класс, который обрабатывает этот queryser
#
# class WorkerAPIUpdate(generics.UpdateAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
