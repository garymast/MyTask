from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Post

# from django.http import HttpResponse

# Create your views here.


class TaskList(ListView):
    model = Post
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Post
    context_object_name = 'task'
    template_name = 'my_tasks/task.html'


class TaskCreate(CreateView):
    model = Post
    fields = '__all__'
    # Also look at adding form class as per CodeInstitute Hello Django
    success_url = reverse_lazy('tasks')
