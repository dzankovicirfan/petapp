# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from pets.models import Pet


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('name', 'birthday', 'owner', 'pet_type')
