# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from account.models import Owner
from pets.serializers import PetSerializer


class OwnerSerializer(serializers.ModelSerializer):
    '''
    Owner Serializer with:
        1.creating and updating passwor option
        2.Owner pets represented as nested objects in Owner API
    '''
    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('username', 'date_joined', 'password', 'pets')

        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'date_joined': {'read_only': True}
        }

    def create(self, validate_data):
        user = super(OwnerSerializer, self).create(validate_data)
        user.set_password(validate_data.get('password'))
        user.save()
        return user

    def update(self, instance, validate_data):
        user = super(OwnerSerializer, self).update(instance, validate_data)

        if validate_data.get('password', None):
            user.set_password(validate_data['password'])
            user.save()
        return user
