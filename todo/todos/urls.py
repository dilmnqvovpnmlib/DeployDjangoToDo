from django.urls import path

from . import views

urlpatterns = [
    path('todo/list/', views.ToDoListView.as_view(), name='todo_list'),
    path('todo/list/<int:pk>', views.ToDoDetailView.as_view(), name='todo_detail'),
    path('todo/delete/<int:pk>', views.ToDoDeleteView.as_view(), name='todo_delete'),
]
