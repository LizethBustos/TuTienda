from django.urls import path
from rest_framework import routers
from .viewsets import ElementViewSet,CategoryViewSet,TypeViewSet
#from django.contrib import admin

route = routers.SimpleRouter()
route.register('element',ElementViewSet)
route.register('category',CategoryViewSet)
route.register('type',TypeViewSet)

urlpatterns = route.urls
