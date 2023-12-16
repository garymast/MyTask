from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post

# from django.http import HttpResponse

# Create your views here.


class TaskList(ListView):
    model = Post
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Post
