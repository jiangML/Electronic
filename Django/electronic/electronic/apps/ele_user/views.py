# -*- coding:utf-8 -*-
from django.http import JsonResponse, Http404
from django.views.generic import View


class EleUser(View):

    def get(self, request, *args, **kwargs):
        a = 'test'
        b = 'hehe'
        return JsonResponse({"test": a, "hehe": b})
