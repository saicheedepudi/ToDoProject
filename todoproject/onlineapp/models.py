# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todolist(models.Model):
    name=models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Todoitems(models.Model):
    description=models.TextField(max_length=500)
    iscomplete=models.BooleanField(default=False)
    dueDate=models.DateField(auto_now_add=False)
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.description

