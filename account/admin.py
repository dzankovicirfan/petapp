# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Owner


admin.site.register(Owner, UserAdmin)
