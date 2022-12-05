from rest_framework import generics, viewsets
from rest_framework.decorators import action

from rest_framework.response import Response
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


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PhotoBaseViewSet(viewsets.ModelViewSet):
    queryset = PhotoBase.objects.all()
    serializer_class = PhotoSerializer


class ControlPointAPIViewDeleteCreate(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    queryset = ControlPoint.objects.all()
    serializer_class = ControlPointSerializer


class CameraAPIViewDeleteCreate(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class ControlListViewSet(viewsets.ModelViewSet):
    queryset = ControlList.objects.all()
    serializer_class = ControlListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer


class VisitTypeAPIView(generics.ListAPIView):
    queryset = VisitType.objects.all()
    serializer_class = VisitTypeSerializer


class VisitJuornalAPIView(generics.ListAPIView, generics.UpdateAPIView):
    queryset = VisitJuornal.objects.all()
    serializer_class = VisitJuornalSerializer

# наследуется от класса котрый определяет набор запросов которые можно использовать
# class WorkerAPIList(generics.ListCreateAPIView):
#     queryset = Worker.objects.all() # данные которые будут возвращаться по эапросу
#     serializer_class = WorkerSerializer # класс, который обрабатывает этот queryser
#
# class WorkerAPIUpdate(generics.UpdateAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
