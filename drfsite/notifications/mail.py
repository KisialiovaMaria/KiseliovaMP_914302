import datetime

from django.contrib.auth.models import User
from workers.models import Notifications
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
anyVisit = 1
nesancts = 2
overAccess = 3
sancts = 4

def sendNotifications(ControlPoint, visitType):
    print(ControlPoint, visitType)
    if visitType.id == 1:
        eventTypes = [anyVisit, sancts]
    elif visitType.id == 3:
        eventTypes = [anyVisit, nesancts]
    elif visitType.id == 2:
        eventTypes = [anyVisit, nesancts, overAccess]
    #users = User.objects.all()
    notifications = []
    for event in eventTypes:
        notifications.extend(list(Notifications.objects.filter(controlPoint=ControlPoint, eventType=event, activity=True)))
    print(notifications)
    for notification in notifications:
        print(notification.userID.email)
        sendNotification(formSendText(notification), notification.userID.email)
def formSendText(notification):
    text = f"Событие: " + str(notification.eventType) +"\nКонтрольный пункт: " + str(notification.controlPoint) + "\nДата: "+ str(datetime.datetime.now())[0:19]
    return text
    # users = ['']
    # reseivers_list = ['']
    # for user in users:
    #     if user in reseivers_list:
    #         sendNotification('бла бла бла', user.email)


def sendNotification(text, reciever_email):
    msg = MIMEMultipart()
    password = "oicusmptarirbvyr"
    msg['From'] = "vcapp55678@gmail.com"
    msg['To'] = reciever_email
    msg['Subject'] = "Subscription"

    message = text
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))