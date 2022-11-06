from rest_framework import serializers
from .models import *

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = (
            "name",
        )

class WorkerSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    position = PositionSerializer() #получаем данные и для FK
    #если встречается choices fiels = serializers.CharField(source='get_service_type_display')
    class Meta:
        model = Worker
        fields = "__all__"



#
# class WorkerSerializerSimple(serializers.Serializer):
#     name = serializers.CharField()
#     position = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Worker.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.position = validated_data.get("position", instance.position)
#         instance.save()
#         return instance