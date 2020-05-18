from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import TagForm, TodoForm
from .models import Tag, Todo


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    context_object_name = 'tags'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(enable=True)
        return queryset


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    context_object_name = 'tags'
    form_class = TagForm
    success_url = reverse_lazy('tag_list')


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    context_object_name = 'tags'
    success_url = reverse_lazy('tag_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.enable = False
        self.object.save()
        return HttpResponseRedirect(self.success_url)


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


class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    context_object_name = 'todo'
    form_class = TodoForm
    # template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ToDoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    context_object_name = 'todo'
    form_class = TodoForm
    template_name = 'todos/todo_update.html'
    success_url = reverse_lazy('todo_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


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
