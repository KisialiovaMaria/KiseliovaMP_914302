"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


import workers.urls
from workers.views import *
from rest_framework import routers


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("workers.urls")),
    # path('api/v1/drf-auth/', include('rest_framework.urls')), #session auth
    # path('api/v1/workerlist', WorkerAPIList.as_view()),
    # path('api/v1/workerlist/<int:pk>', WorkerAPIUpdate.as_view()),
    # path('api/v1/workerdetail/<int:pk>', WorkerAPIDetailView.as_view()),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
