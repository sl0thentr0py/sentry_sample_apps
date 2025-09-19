"""sentry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from errors.views import bork, transaction, rq_task, celery_task, scope1, scope2, sync_to_async_test, sync_to_async_test_not_sensitive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('errors/', bork),
    path('scope1/', scope1),
    path('scope2/', scope2),
    path('transaction/<int:num>', transaction),
    path('rq_task/', rq_task),
    path('celery_task/', celery_task),
    path('sync_to_async/', sync_to_async_test),
    path('sync_to_async_not/', sync_to_async_test_not_sensitive),
]
