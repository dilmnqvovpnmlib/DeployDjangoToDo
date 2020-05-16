from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoListView.as_view(), name='index'),
]
