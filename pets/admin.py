# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = list_display_links = ['name', 'birthday', 'owner', 'pet_type']


admin.site.register(Pet, PetAdmin)
