import json
import unittest

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from workers.models import User, Department, Position, Worker, ControlPoint
from workers.Serializers import DepartmentSerializer, PositionSerializer
from workers.views import UserViewSet

import logging
logger = logging.getLogger(__name__)
class WorkerTests(APITestCase):

    def setUp(self):
        Department.objects.create(departmentName="test")
        Position.objects.create(positionName="test")
        User.objects.create(username="username", password="pass")
        ControlPoint.objects.create(name="test")
        self.add_test_worker()
        user = User.objects.get(username='username')
        self.client.force_authenticate(user=user)

    def add_test_worker(self):
        new_worker = Worker(
            name="Name",
            surname="Surname",
            patronymic="Pat",
            phone=3445885,
            email="ginga@mail.ru",
            department=Department.objects.all()[0],
            position=Position.objects.all()[0]
        )
        new_worker.save()

    def delete_all_workers(self):
        Worker.objects.all().delete()

    def test_list_worker(self):
        url = "/api/v1/workers/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_worker(self):
        id = Worker.objects.get().id
        url = f"/api/v1/workers/{id}/"
        data = {
            "name": "Мария4",
            "surname": "new",
            "patronymic": "new",
            "phone": 343432444,
            "email": "ma@mail1.ru",
            "position": "test",
            "department": "test",
            "controlPoints": [
            ]
        }
        response = self.client.put(path=url, data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Worker.objects.count(), 1)
        self.assertEqual(Worker.objects.get().name, 'Мария4')
        self.assertEqual(Worker.objects.get().surname, 'new')
        self.assertEqual(Worker.objects.get().phone, 343432444)
        self.assertEqual(Worker.objects.get().email, 'ma@mail1.ru')
        self.assertEqual(Worker.objects.get().position, Position.objects.get(positionName="test"))
        self.assertEqual(Worker.objects.get().department, Department.objects.get(departmentName="test"))

    def test_change_access_list(self):
        id = Worker.objects.get().id
        url = f"/api/v1/workers/{id}/"
        data = {
            "controlPoints": [
                1
            ]
        }
        response = self.client.patch(path=url, data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Worker.objects.count(), 1)
        self.assertEqual(Worker.objects.get().controlPoints.count(), 1)

    def test_delete_worker(self):
        id = Worker.objects.get().id
        url = f"/api/v1/workers/{id}/"
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Worker.objects.count(), 0)

    def test_create_worker(self):
        self.delete_all_workers()
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


class NotificationsTests(APITestCase):
    def setUp(self):
        pass

    def test_create_notification(self):
        pass

    def test_turn_on_notification(self):
        pass
