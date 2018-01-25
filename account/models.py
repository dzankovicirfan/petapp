# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser


class Owner(AbstractUser):
    '''
    Using AbstracUser from django models for creating our Owner model
    '''

    class Meta:
        verbose_name = 'owner'
        verbose_name_plural = 'owners'
