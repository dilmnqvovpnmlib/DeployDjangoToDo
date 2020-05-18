from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView

from .models import Todo


class ToDoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todos'
    # アプリ名/モデル名_list.htmlが設定されて入れば書かんくてもOK
    # template_name = 'todos/todos_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user).filter(enable=True)
        return queryset


class ToDoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'todo'
    # template_name = 'todos/todo_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class ToDoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'todo'
    # template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.enable = False
        self.object.save()
        return HttpResponseRedirect(self.success_url)
