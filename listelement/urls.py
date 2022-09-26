from django.urls import path
from rest_framework import routers
from .viewsets import ElementViewSet
#from django.contrib import admin

route = routers.SimpleRouter()
route.register('element',ElementViewSet)

urlpatterns = route.urls
