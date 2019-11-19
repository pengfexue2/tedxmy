from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WebsiteSerializer
from .models import Website


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer