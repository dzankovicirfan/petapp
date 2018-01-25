# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet

from pets.serializers import PetSerializer
from pets.models import Pet


class PetView(ModelViewSet):
    '''
    Pet View with filter fields by:
        1. pet_type
        2. owner
    '''
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_fields = ('pet_type', 'owner')
