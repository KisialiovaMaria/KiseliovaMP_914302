import threading
from datetime import time

import cv2
from django.http import StreamingHttpResponse, JsonResponse, HttpResponse
from django.shortcuts import render
from dns.transaction import ReadOnly
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action, api_view
from django.db.models import Q
from django.views.decorators import gzip
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from FR.face_recognition_block import FaceRecognizer, gen
from .models import *
from .Serializers import *


# from rest_framework import viewsets


# APIView готовое
class WorkerViewSet(viewsets.ModelViewSet):  # предоставляет все CRUD
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerPutAPIView(generics.UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerExceptListView(generics.ListAPIView):
    # queryset = Worker.objects.filter(controlPoints = 1)
    serializer_class = WorkerSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['pk']
        return Worker.objects.filter(~Q(controlPoints=id))
    # def get(self, *args, **kwargs):
    #     ControlPointID = kwargs['pk']
    #     return Worker.objects.filter(controlPoints = ControlPointID)


class ControlPointViewSet(viewsets.ModelViewSet):
    queryset = ControlPoint.objects.all()
    serializer_class = ControlPointSerializer


class ControlPointWholeViewSet(viewsets.ModelViewSet):
    queryset = ControlPoint.objects.all()
    serializer_class = ControlPointWholeSerializer

class PositionAPIView(generics.ListAPIView):
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


class JuornalAPIListPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 1000
class JuornalAPIListView(generics.ListAPIView):
    queryset = VisitJuornal.objects.all()
    serializer_class = VisitJuornalWholeSerializer
    pagination_class = JuornalAPIListPagination

class VisitJuornalAPIView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = VisitJuornal.objects.all()
    serializer_class = VisitJuornalSerializer

class VisitJuornalWholeAPIView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = VisitJuornal.objects.all()
    serializer_class = VisitJuornalWholeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoSerializer:
    pass


class UserFindAPIView(generics.ListAPIView):
    #queryset = User.objects.filter(username='masha')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)

class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer

class NotificationsByUserAPIListView(generics.ListAPIView):
    serializer_class = NotificationsSerializer
    def get_queryset(self):
        username = self.kwargs['pk']
        return Notifications.objects.filter(userID=username)

FACE_RECOGNIZERS = []

@api_view(['GET'])
def FaceRecognitionStart(request, *args, **kwargs):

    if request.method == 'GET':

        all_workers = Worker.objects.all()
        all_workers_images_paths = []
        all_workers_ids = []
        for worker in all_workers:
            if(worker.photo):
                all_workers_images_paths.append('./media/'+str(worker.photo))
                all_workers_ids.append(worker.id)

        try:
            fr = FaceRecognizer(all_workers_images_paths, all_workers_ids, kwargs['pk'])
            fr.start_recognition()
            FACE_RECOGNIZERS.append(fr)

            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def FaceRecognitionStop(request, *args, **kwargs):
    if request.method == 'GET':
        try:
            FACE_RECOGNIZERS[0].stop_recognition()
            FACE_RECOGNIZERS.pop(0)
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def VideoTranslationnStart(request, *args, **kwargs):
    if request.method == 'GET':
        try:
            # f_recognizer.start_video_representing()
            # f_recognizer.stop_video_representing()
            # gen(cam)
            #FACE_RECOGNIZERS[0].stop_video_representing()
            FACE_RECOGNIZERS[0].start_video_representing()


            return StreamingHttpResponse(gen(FACE_RECOGNIZERS[0]),
                                         content_type='multipart/x-mixed-replace;boundary=frame')
        except:
            return Response({"error": "((("})

# class FaceRecognitionStartView(Request):
#
#         try:
#             # cam = VideoCamera()
#
#             FACE_RECOGNIZER = FR.face_recognition_block.FaceRecognizer(['./FR/images/masha.png', './FR/images/obama.png'], ['1', '2'])
#             # f_recognizer.start_video_representing()
#             # f_recognizer.stop_video_representing()
#             # gen(cam)
#             FACE_RECOGNIZER.start_recognition()
#
#             # return StreamingHttpResponse(FR.face_recognition_block.gen(cam2),
#             #                              content_type='multipart/x-mixed-replace;boundary=frame')
#         except:
#             pass
#
# def FaceRecognitionStopView(Request):
#     try:
#         FACE_RECOGNIZER.stop_recognition()
#     except:
#         pass
#

# @gzip.gzip_page
# def VideoPresentation(reqest):
#     try:
#         # cam = VideoCamera()
#
#         cam2 = FR.face_recognition_block.FaceRecognizer(['./FR/images/masha.png', './FR/images/obama.png'], ['1', '2'])
#         cam2.start_video_representing()
#         for _ in range(1000):
#             pass
#         print('stop')
#         cam2.stop_video_representing()
#         # gen(cam)
#         # cam2.start_recognition()
#
#         return StreamingHttpResponse(FR.face_recognition_block.gen(cam2),
#                                      content_type='multipart/x-mixed-replace;boundary=frame')
#     except:
#         pass
#     return render(reqest, 'C:/Users/masha/PycharmProjects/rest_api_workers/drfsite/workers/workers.html')
#
#
# @gzip.gzip_page
# def Home(reqest):
#     try:
#         # cam = VideoCamera()
#
#         cam2 = FR.face_recognition_block.FaceRecognizer(['./FR/images/masha.png', './FR/images/obama.png'], ['1', '2'])
#         cam2.start_video_representing()
#         for _ in range(1000):
#             pass
#         print('stop')
#         cam2.stop_video_representing()
#         # gen(cam)
#         # cam2.start_recognition()
#
#         return StreamingHttpResponse(FR.face_recognition_block.gen(cam2),
#                                      content_type='multipart/x-mixed-replace;boundary=frame')
#     except:
#         pass
#     return render(reqest, 'C:/Users/masha/PycharmProjects/rest_api_workers/drfsite/workers/workers.html')

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
class VisitTypeAPIView(generics.ListAPIView):
    queryset = VisitType.objects.all()
    serializer_class = VisitTypeSerializer




# наследуется от класса котрый определяет набор запросов которые можно использовать
# class WorkerAPIList(generics.ListCreateAPIView):
#     queryset = Worker.objects.all() # данные которые будут возвращаться по эапросу
#     serializer_class = WorkerSerializer # класс, который обрабатывает этот queryser
#
# class WorkerAPIUpdate(generics.UpdateAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
