from django.shortcuts import render
from django.views.generic import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = dict()
        return render(request, "homepage/index.html", context)