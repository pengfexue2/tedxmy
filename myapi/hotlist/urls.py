#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-11-18 16:35

__author__ = 'Ted'


from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'website',views.WebsiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
