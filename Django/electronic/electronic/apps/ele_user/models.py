# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class EleUser(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
#    regist_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username
