# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Todolist
from .models import Todoitems
admin.site.register(Todolist)
admin.site.register(Todoitems)