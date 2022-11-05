from rest_framework import serializers
from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Worker
        fields = (
            "name",
            "position",
        )
        # fields = "__all__"
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