from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView


class ToDoListView(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the polls index.")
