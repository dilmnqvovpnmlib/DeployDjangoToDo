from django.urls import path

from . import views

urlpatterns = [
    path('todo/list/', views.ToDoListView.as_view(), name='todo_list'),
    path('todo/list/<int:pk>', views.ToDoDetailView.as_view(), name='todo_detail'),
    path('todo/create/', views.ToDoCreateView.as_view(), name='todo_create'),
    path('todo/update/<int:pk>', views.ToDoUpdateView.as_view(), name='todo_update'),
    path('todo/delete/<int:pk>', views.ToDoDeleteView.as_view(), name='todo_delete'),
]
