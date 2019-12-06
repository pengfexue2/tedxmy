from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WebsiteSerializer, WeiboSerializer
from .models import Website, Weibo


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer


class WeiboViewSet(viewsets.ModelViewSet):
    queryset = Weibo.objects.all()
    serializer_class = WeiboSerializer