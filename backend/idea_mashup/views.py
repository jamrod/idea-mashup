from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Who, What, Where, Why
from .serializers import WhoSerializer, WhatSerializer, WhereSerializer, WhySerializer
import random


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


class IdeaView(APIView):
    """
    Get one random value from each table
    """

    def get(self, request):
        who = random.choice(Who.objects.all())
        serializedWho = WhoSerializer(who)
        what = random.choice(What.objects.all())
        serializedWhat = WhatSerializer(what)
        return Response({
            'who': serializedWho.data,
            'what': serializedWhat.data,
        })
