from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action

from .models import Worker, Position
from .Serializers import WorkerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Worker
from django.forms import model_to_dict
#from rest_framework import viewsets


# APIView


class WorkerViewSet(viewsets.ModelViewSet): #предоставляет все CRUD
    #queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get_queryset(self):
        return Worker.objects.all()[:3]

    @action(methods=['get'], detail=True) # detail=True для одного False для всех
    def position(self, request, pk=None):
        positions = Position.objects.get(pk=pk)
        return Response({'cats':positions.name})

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
class WorkerAPIView(APIView):
    def get(self, request):
        worker_list = Worker.objects.all()
        return Response({'workers':WorkerSerializer(worker_list, many=True).data})

    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'was_posted':serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Worker.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
        serializer = WorkerSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        return Response({"post": serializer.data})


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
