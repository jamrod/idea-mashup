from rest_framework import serializers
from .models import Who, What, Where, Why


class WhoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Who
        fields = ['data']


class WhatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = What
        fields = ['data']


class WhereSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Where
        fields = ['data']


class WhySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Why
        fields = ['data']
