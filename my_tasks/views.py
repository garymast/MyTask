from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# from django.http import HttpResponse

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'my_tasks/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'tasks'


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'task'
    template_name = 'my_tasks/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'
    # Also look at adding form class as per CodeInstitute Hello Django
    success_url = reverse_lazy('tasks')
    # 2013-06-26 00:14:26.260524 Example Date Time String


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
