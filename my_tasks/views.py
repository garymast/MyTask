from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Post

# from django.http import HttpResponse

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'my_tasks/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'my_tasks/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        author = form.save()
        if author is not None:
            login(self.request, author)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(author=self.request.user)
        context['count'] = context['tasks'].filter(done=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__istartswith=search_input
            )

        context['search_input'] = search_input

        return context
    # Look at creating user groups in the future


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'task'
    template_name = 'my_tasks/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'done', 'priority', 'due_date']
    # Also look at adding form class as per CodeInstitute Hello Django
    success_url = reverse_lazy('tasks')
    # 2013-06-26 00:14:26.260524 Example Date Time String
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'done', 'priority', 'due_date']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
