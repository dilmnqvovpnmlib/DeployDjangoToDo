from django.shortcuts import render

from django.views.generic import ListView
from django.http import HttpResponse

class UserListView(ListView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the polls index.")
