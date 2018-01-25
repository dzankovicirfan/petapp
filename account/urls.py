# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include
from rest_framework import routers

from account.views import OwnerView

router = routers.DefaultRouter()
router.register(r'account', OwnerView)

app_name = 'account'
urlpatterns = [
    path('', include(router.urls)),
]
