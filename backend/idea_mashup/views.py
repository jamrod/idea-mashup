from django.shortcuts import render
from rest_framework import viewsets
from .models import Who, What, Where, Why
from .serializers import WhoSerializer, WhatSerializer, WhereSerializer, WhySerializer


class WhoViewSet(viewsets.ModelViewSet):
    queryset = Who.objects.all()
    serializer_class = WhoSerializer


class WhatViewSet(viewsets.ModelViewSet):
    queryset = What.objects.all()
    serializer_class = WhatSerializer


class WhereViewSet(viewsets.ModelViewSet):
    queryset = Where.objects.all()
    serializer_class = WhereSerializer


class WhyViewSet(viewsets.ModelViewSet):
    queryset = Why.objects.all()
    serializer_class = WhySerializer
