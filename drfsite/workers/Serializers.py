import account as account
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
    workers = WorkerSerializer(many=True)
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
    # roleID = RoleSerializer()
    # workerID = WorkerSerializer()
    #password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_active=True,
        )
        return user
    class Meta:
        model = User
        fields = ["id", "password", "username", "first_name", "last_name", "email", "is_superuser", "is_active"]
        #fields = "__all__"


class VisitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitType
        fields = "__all__"
class NotificationsSerializer(serializers.ModelSerializer):
    userID = SlugRelatedField("username", queryset=User.objects.all(), allow_null=True)
    eventType = SlugRelatedField("eventType", queryset=EventType.objects.all())
    controlPoint = SlugRelatedField("name", queryset=ControlPoint.objects.all())

    class Meta:
        model = Notifications
        fields = "__all__"
class NotificationsWholeSerializer(serializers.ModelSerializer):
    userID = UserSerializer()
    eventType = EventTypeSerializer()
    controlPoint = ControlPointSerializer()

    class Meta:
        model = Notifications
        fields = "__all__"


class VisitJuornalSerializer(serializers.ModelSerializer):
    personID = SlugRelatedField("id", queryset=Worker.objects.all(), allow_empty=True, allow_null=True)
    #fixedPhotoID = PhotoBaseSerializer(allow_null=True)
    controlPointID = SlugRelatedField("id", queryset=ControlPoint.objects.all())
    visitTypeID = SlugRelatedField("visitTypeName", queryset=VisitType.objects.all())

    class Meta:
        model = VisitJuornal
        fields = "__all__"

class VisitJuornalWholeSerializer(serializers.ModelSerializer):
    personID = WorkerSerializer()
    #fixedPhotoID = PhotoBaseSerializer(allow_null=True)
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
