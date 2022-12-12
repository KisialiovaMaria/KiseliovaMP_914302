from django.contrib import admin
from .models import *

admin.site.register(Worker)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(EventType)
admin.site.register(SendType)
admin.site.register(ControlPoint)

admin.site.register(PhotoBase)
admin.site.register(VisitType)
admin.site.register(Role)
admin.site.register(Notifications)
