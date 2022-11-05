from django.db import models


# Create your models here.
#from rest_framework.authtoken.admin import User
from django.contrib.auth.models import User

class Position(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name
class Worker(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT, null=True)
    #user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def _str__(self):
        return self.title + "  " + self.cat.name




