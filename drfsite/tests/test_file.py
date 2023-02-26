import json

from rest_framework import status
from rest_framework.test import APITestCase
from workers.models import *


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
        print(response)
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
        print(response)
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
        control_point_id = ControlPoint.objects.get().id
        data = {
            "controlPoints": [
                control_point_id
            ]
        }
        response = self.client.patch(path=url, data=json.dumps(data), content_type="application/json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Worker.objects.count(), 1)
        self.assertEqual(Worker.objects.get().controlPoints.count(), 1)

    def test_delete_worker(self):
        id = Worker.objects.get().id
        url = f"/api/v1/workers/{id}/"
        response = self.client.delete(path=url)
        print(response)
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
        print(response)
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
        Department.objects.create(departmentName="test")
        Position.objects.create(positionName="test")
        User.objects.create(username="username", password="pass")
        ControlPoint.objects.create(name="test")
        EventType.objects.create(eventType="test_type")
        user = User.objects.get(username='username')
        self.client.force_authenticate(user=user)


    def test_create_notification(self):
        url = "/api/v1/notifications/"
        username = User.objects.get().username
        eventType = EventType.objects.get().eventType
        control_point = ControlPoint.objects.get().name
        data = {
            "user": username,
            "eventType": eventType,
            "controlPoint": control_point,
            "activity": False
        }
        response = self.client.post(path=url, data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notifications.objects.count(), 1)
        self.assertEqual(Notifications.objects.get().user, User.objects.get())
        self.assertEqual(Notifications.objects.get().controlPoint, ControlPoint.objects.get())

    def test_turn_on_notification(self):
        self.test_create_notification()
        notification_id = Notifications.objects.get().id
        url = f"/api/v1/notifications/{notification_id}/"
        data = {
            "activity": True
        }
        response=self.client.patch(path=url, data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Notifications.objects.get().activity, True)

    def test_delete_notification(self):
        self.test_create_notification()
        notification_id = Notifications.objects.get().id
        url = f"/api/v1/notifications/{notification_id}/"
        response = self.client.delete(path=url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Notifications.objects.count(), 0)

class JuornalTests(APITestCase):
    def setUp(self):
        Department.objects.create(departmentName="test")
        Position.objects.create(positionName="test")
        User.objects.create(username="username", password="pass")
        ControlPoint.objects.create(name="test")
        VisitType.objects.create(visitTypeName="test_type")
        self.add_test_worker()
        self.add_visit()
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


    def add_visit(self):
        visit = VisitJuornal(
            person=Worker.objects.get(),
            controlPoint=ControlPoint.objects.get(),
            visitType=VisitType.objects.get(),
        )
        visit.save()
    def test_list_juornal(self):
        url = "/api/v1/visit-juornal/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ControlPointsTests(APITestCase):
    def setUp(self):
        ControlPoint.objects.create(name="test")
        User.objects.create(username="username", password="pass")
        Department.objects.create(departmentName="test")
        Position.objects.create(positionName="test")
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

    def test_create_control_point(self):
        ControlPoint.objects.all().delete()
        url = f"/api/v1/control-points/"
        data = {
            "name": "test",
            "camera_activity": False,
            "camera_name": "test",
            "workers": []
        }
        response = self.client.post(path=url, data=json.dumps(data), content_type="application/json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ControlPoint.objects.count(), 1)
        self.assertEqual(ControlPoint.objects.get().name, "test")
        self.assertEqual(ControlPoint.objects.get().camera_activity, False)
        self.assertEqual(ControlPoint.objects.get().camera_name, "test")

        pass

    def test_delete_control_point(self):
        control_point_id = ControlPoint.objects.get().id
        url = f"/api/v1/control-points/{control_point_id}/"
        response = self.client.delete(path=url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ControlPoint.objects.count(), 0)

    def test_activate_face_recognition(self):
        control_point_id = ControlPoint.objects.get().id
        url = f"/api/v1/face-recognition/start/{control_point_id}/"
        print(url)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.get(path=f"/api/v1/face-recognition/stop/{control_point_id}/")

    def test_change_access_list(self):
        control_point_id = ControlPoint.objects.get().id
        worker_id = Worker.objects.get().id
        url = f"/api/v1/control-points/{control_point_id}/"
        data = {
            "workers": [
                worker_id
            ]
        }
        response = self.client.patch(path=url, data=json.dumps(data), content_type="application/json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ControlPoint.objects.get().workers.count(), 1)
