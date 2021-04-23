"""codr URL Configuration

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
import django
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from codrs.views import ArrayViewSet, PushViewSet, ProfileViewSet

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'array', ArrayViewSet) 
router.register(r'push', PushViewSet) 
router.register(r'profile', ProfileViewSet) 


urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('login/', include(django.contrib.auth.urls))
]