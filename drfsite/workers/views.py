from rest_framework import generics, viewsets
from rest_framework.decorators import action

from rest_framework.response import Response
from .models import *
from .Serializers import *
#from rest_framework import viewsets


# APIView


class WorkerViewSet(viewsets.ModelViewSet): #предоставляет все CRUD
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    # def get_queryset(self):
    #     return Worker.objects.all()[:3]

    # @action(methods=['get'], detail=True) # detail=True для одного False для всех
    # def position(self, request, pk=None):
    #     positions = Position.objects.get(pk=pk)
    #     return Response({'cats':positions.name})

class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

# наследуется от класса котрый определяет набор запросов которые можно использовать
# class WorkerAPIList(generics.ListCreateAPIView):
#     queryset = Worker.objects.all() # данные которые будут возвращаться по эапросу
#     serializer_class = WorkerSerializer # класс, который обрабатывает этот queryser
#
# class WorkerAPIUpdate(generics.UpdateAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
#
#
# class WorkerAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
# # Create your views here.


# class WorkerAPIList(generics.ListCreateAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer

#
# class WorkerAPIUpdate(generics.UpdateAPIView):
#     queryset = Worker.objects.all()  # возвращает одну запись а не все, тк ленивый запрос
#     serializer_class = WorkerSerializer
#
#
# class WorkerAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
