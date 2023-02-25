import json
import unittest

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from workers.models import User, Department, Position, Worker
from workers.Serializers import DepartmentSerializer, PositionSerializer
from workers.views import UserViewSet


class WorkerTests(APITestCase):
    def setUp(self):
        Department.objects.create(departmentName="test")
        Position.objects.create(positionName="test")
        User.objects.create(username="username", password="pass")
        user = User.objects.get(username='username')
        self.client.force_authenticate(user=user)

    def test_create_worker(self):
        url = "/api/v1/workers/"
        data = {
            "name": "Мария2",
            "surname": "Киселёва",
            "patronymic": "Павловна",
            "phone": 343432432,
            "email": "ma@mail.ru",
            "position": "test",
            "department": "test",
            "controlPoints": [
            ]
        }

        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Worker.objects.count(), 1)
        self.assertEqual(Worker.objects.get().name, 'Мария2')
        self.assertEqual(Worker.objects.get().surname, 'Киселёва')
        self.assertEqual(Worker.objects.get().phone, 343432432)
        self.assertEqual(Worker.objects.get().email, 'ma@mail.ru')
        self.assertEqual(Worker.objects.get().position, Position.objects.get(positionName="test"))
        self.assertEqual(Worker.objects.get().department, Department.objects.get(departmentName="test"))

    def test_delete_worker(self):
        pass

    def test_update_worker(self):
        pass

    def test_change_access_list(self):
        pass

    def test_list_worker(self):
        pass


class NotificationsTests(APITestCase):
   def setUp(self):
       pass

   def test_create_notification(self):
       pass

   def test_turn_on_notification(self):
       pass

