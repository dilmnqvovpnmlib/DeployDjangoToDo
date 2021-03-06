from django.urls import path

from . import views

urlpatterns = [
    path('tag/list/', views.TagListView.as_view(), name='tag_list'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag/delete/<int:pk>', views.TagDeleteView.as_view(), name='tag_delete'),
    path('todo/list/', views.ToDoListView.as_view(), name='todo_list'),
    path('todo/list/<int:pk>', views.ToDoDetailView.as_view(), name='todo_detail'),
    path('todo/create/', views.ToDoCreateView.as_view(), name='todo_create'),
    path('todo/update/<int:pk>', views.ToDoUpdateView.as_view(), name='todo_update'),
    path('todo/delete/<int:pk>', views.ToDoDeleteView.as_view(), name='todo_delete'),
]
