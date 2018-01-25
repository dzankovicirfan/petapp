# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include
from rest_framework import routers

from pets.views import PetView

router = routers.DefaultRouter()
router.register(r'pets', PetView)

app_name = 'pets'
urlpatterns = [
    path('', include(router.urls)),
]
