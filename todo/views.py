from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

class TodoList(ListView):
    model = TodoModel
    template_name = "list.html"

class TodoDetail(DetailView):
    model = TodoModel
    template_name = "detail.html"

class TodoCreate(CreateView):
    model = TodoModel
    template_name = "create.html"
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    model = TodoModel
    template_name = "delete.html"
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    model = TodoModel
    template_name = "update.html"
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
