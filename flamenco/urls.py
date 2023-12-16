"""
URL configuration for flamenco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from my_tasks import views as index_views
from my_tasks.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signin/', CustomLoginView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(next_page='signin'), name='signout'),
    path('signup/', RegisterPage.as_view(), name='signup'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('update-task<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete-task<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('admin/', admin.site.urls),
]
