#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import EleUser


urlpatterns = [
    url(r'^user/$',
        EleUser.as_view(),
        name="EleUser",
        ),
]
