from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post

# from django.http import HttpResponse

# Create your views here.


class TaskList(ListView):
    model = Post
