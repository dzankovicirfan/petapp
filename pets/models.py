# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Owner


class Pet(models.Model):
    '''
    Pet model with 2 types, and Owner as Foreign Key
    '''
    PET_TYPES = (
        (1, 'Dog'),
        (2, 'Cat')
    )
    name = models.CharField('Name', max_length=50)
    birthday = models.DateField('Birthday')
    owner = models.ForeignKey(Owner, related_name='pets', on_delete=models.CASCADE)
    pet_type = models.IntegerField(choices=PET_TYPES)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'pet'
        verbose_name_plural = 'pets'
