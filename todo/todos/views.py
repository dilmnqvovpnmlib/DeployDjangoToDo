from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Todo


class ToDoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'todos/todo_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
