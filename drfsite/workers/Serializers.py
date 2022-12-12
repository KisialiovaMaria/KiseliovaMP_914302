from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField

from .models import *


# class PositionSerializer1(serializers.ModelSerializer):
#     class Meta:
#         model = Position
#         fields = (
#             "name",
#         )
#
#
# class WorkerSerializer1(serializers.ModelSerializer):
#     # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     position = PositionSerializer1()  # получаем данные и для FK
#
#     # если встречается choices fiels = serializers.CharField(source='get_service_type_display')
#     class Meta:
#         model = Worker
#         fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"


class SendTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendType
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class WorkerSerializer(serializers.ModelSerializer):
    positionID = SlugRelatedField("positionName", queryset=Position.objects.all())
    departmentID = SlugRelatedField("departmentName", queryset=Department.objects.all())

    class Meta:
        model = Worker
        fields = ['id','name','surname','patronymic','phone', 'email','positionID','departmentID','photo','controlPoints']
        #extra_kwargs = {'controlPoints': {'required': False}}

#
# class PhotoSerializer(serializers.ModelSerializer):
#     workerID = WorkerSerializer()
#
#     class Meta:
#         model = Photo
#         fields = "__all__"

class ControlPointSerializer(serializers.ModelSerializer):
    #workers = WorkerSerializer(many=True, read_only=True)
    #workers = SlugRelatedField("id", queryset=Worker.objects.all())
    class Meta:
        model = ControlPoint
        fields = ['id','name','camera_activity','camera_name','workers']
        extra_kwargs = {'workers': {'required': False}}


class ControlPointWholeSerializer(serializers.ModelSerializer):
    workers = WorkerSerializer(many=True, read_only=True)
    #workers = SlugRelatedField("id", queryset=Worker.objects.all())
    class Meta:
        model = ControlPoint
        fields = ['id','name','camera_activity','camera_name','workers']

class PhotoBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoBase
        fields = "__all__"





class ControlPointUpdateCameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlPoint
        fields = ['camera_activity']





# class CameraSerializer(serializers.ModelSerializer):
#     controlPointID = ControlPointSerializer()
#     class Meta:
#         model = Camera
#         fields = "__all__"
#

# class ControlListSerializer(serializers.ModelSerializer):
#     worker = WorkerSerializer()
#     controlPoint = ControlPointSerializer()
#     class Meta:
#         model = ControlList
#         fields = "__all__"

# class ControlPointWorkerListSerializer(serializers.ModelSerializer):
#     worker = WorkerSerializer()
#     class Meta:
#         model = ControlList
#         fields = ["worker"]


class UserSerializer(serializers.ModelSerializer):
    roleID = RoleSerializer()
    workerID = WorkerSerializer()

    class Meta:
        model = User
        fields = "__all__"


class NotificationsSerializer(serializers.ModelSerializer):
    userID = UserSerializer()

    class Meta:
        model = Notifications
        fields = "__all__"


class VisitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitType
        fields = "__all__"


class VisitJuornalSerializer(serializers.ModelSerializer):
    personID = WorkerSerializer()
    fixedPhotoID = PhotoBaseSerializer()
    controlPointID = ControlPointSerializer()
    visitTypeID = VisitTypeSerializer()

    class Meta:
        model = VisitJuornal
        fields = "__all__"

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
