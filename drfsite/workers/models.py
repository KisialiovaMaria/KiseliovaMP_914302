from django.db import models

# Create your models here.
# from rest_framework.authtoken.admin import User
from django.contrib.auth.models import User


# class Position(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     def __str__(self):
#         return self.name
# class Worker(models.Model):
#     name = models.CharField(max_length=255)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     position = models.ForeignKey(Position, on_delete=models.PROTECT, null=True)
#     #user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
#
#     def _str__(self):
#         return self.title + "  " + self.cat.name
class Position(models.Model):
    positionName = models.CharField(max_length=20)

    def __str__(self):
        return self.positionName


class Department(models.Model):
    departmentName = models.CharField(max_length=20)

    def __str__(self):
        return self.departmentName


class EventType(models.Model):
    eventType = models.CharField(max_length=20)

    def __str__(self):
        return self.eventType


class SendType(models.Model):
    sendType = models.CharField(max_length=20)

    def __str__(self):
        return self.sendType


class Role(models.Model):
    rolename = models.CharField(max_length=20)

    def __str__(self):
        return self.rolename

# class Photo(models.Model):
#     photo = models.ImageField(upload_to=f"workers_images/")
#     def __str__(self):
#         return str(self.workerID)
def worker_photo_directory_path(instance, filename):
    return f'workers_images/{instance.id}/{filename}'
class Worker(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=25)
    patronymic = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=25)
    positionID = models.ForeignKey(Position, on_delete=models.NOT_PROVIDED)
    departmentID = models.ForeignKey(Department, on_delete=models.NOT_PROVIDED)
    #photo = models.ForeignKey(Photo, on_delete=models.SET_NULL())
    photo = models.ImageField(upload_to=worker_photo_directory_path, null=True)

    def __str__(self):
        return self.name + self.surname






class PhotoBase(models.Model):
    photo = models.ImageField()


class ControlPoint(models.Model):
    name = models.CharField(max_length=20)
    camera_name = models.CharField(max_length=20, default="fff")
    camera_activity = models.BooleanField(default=False)
    workers = models.ManyToManyField(Worker, through="ControlList")
    def __str__(self):
        return self.name


# class Camera(models.Model):
#     ipAdress = models.CharField(max_length=15)
#     name = models.CharField(max_length=20)
#     controlPointID = models.OneToOneField(ControlPoint, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name + self.ipAdress
#

class ControlList(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    controlPoint = models.ForeignKey(ControlPoint, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('worker', 'controlPoint')
    def __str__(self):
        return self.controlPoint.__str__() + " --- "+self.worker.__str__()


class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    activity = models.BooleanField()
    roleID = models.ForeignKey(Role, on_delete=models.NOT_PROVIDED)
    workerID = models.ForeignKey(Worker, on_delete=models.NOT_PROVIDED)

    def __str__(self):
        return self.login + self.password


class Notifications(models.Model):
    sendTypeID = models.ForeignKey(SendType, on_delete=models.CASCADE)
    eventTypeID = models.ForeignKey(EventType, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.BooleanField(null=True)

    def __str__(self):
        return self.sendTypeID + self.eventTypeID + self.userID


class Report(models.Model):
    title = models.CharField(max_length=20)
    periodFrom = models.DateField()
    periodTo = models.DateField()
    authID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class VisitType(models.Model):
    visitTypeName = models.CharField(max_length=20)

    def __str__(self):
        return self.visitTypeName


class VisitJuornal(models.Model):
    date = models.DateTimeField(auto_now=True)
    personID = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    fixedPhotoID = models.ForeignKey(PhotoBase, on_delete=models.SET_NULL, null=True)
    controlPointID = models.ForeignKey(ControlPoint, on_delete=models.CASCADE)
    visitTypeID = models.ForeignKey(VisitType, on_delete=models.NOT_PROVIDED)

    def __str__(self):
        return self.date + self.personID + self.visitTypeID
