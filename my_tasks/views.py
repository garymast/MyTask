from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Post
from django import forms
from .forms import ItemForm

from django.contrib import messages

# from django.http import HttpResponse

# Create your views here.


class CustomLoginView(LoginView):
    template_name = "my_tasks/signin.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")

    def form_valid(self, form):
        messages.success(self.request, "Login Successful")
        return super().form_valid(form)


class RegisterPage(FormView):
    template_name = "my_tasks/signup.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        messages.success(self.request, "Registration Successful")
        author = form.save()
        if author is not None:
            login(self.request, author)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "tasks"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['tasks'] = context['tasks'].filter(author=self.request.user)
        context["count"] = context["tasks"].filter(done=False).count()
        

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__istartswith=search_input)

        context["search_input"] = search_input

        return context


    # Look at creating user groups in the future


def task_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully")
            return redirect("tasks")
        else:
            messages.warning(request, "Due date cannot be earlier than today.")

    form = ItemForm()
    context = {"form": form}
    return render(request, "my_tasks/post_form.html", context)


def edit_item(request, item_id):
    item = get_object_or_404(Post, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully")
            return redirect("tasks")
    form = ItemForm(instance=item)
    context = {"form": form, "task": item}
    return render(request, "my_tasks/post_form.html", context)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = "task"
    success_url = reverse_lazy("tasks")


    def form_valid(self, form):
        messages.success(self.request, "Task deleted successfully")
        return super().form_valid(form)


def toggle_item(request, item_id):
    item = get_object_or_404(Post, id=item_id)
    item.done = not item.done
    item.save()
    if item.done:
        messages.success(request, "Task marked as Complete")
    else:
        messages.success(request, "Task marked as Not Done")

    return redirect("tasks")
