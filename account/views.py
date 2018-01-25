# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet

from account.serializers import OwnerSerializer
from account.models import Owner


class OwnerView(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
