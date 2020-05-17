from django.urls import path

from . import views

urlpatterns = [
    path('todo/list/', views.ToDoListView.as_view(), name='todo_list'),
]
