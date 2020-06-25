from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'who', views.WhoViewSet)
router.register(r'what', views.WhatViewSet)
router.register(r'where', views.WhereViewSet)
router.register(r'why', views.WhyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
