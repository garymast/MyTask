from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib import messages
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

STATUS = ((0, "Draft"), (1, "Published"))
PRIO = ((0, "Low"), (1, "Medium"), (2, "High"))

# Create your models here.

# def validate_date(due_date):
#         if due_date < timezone.now().date():
#             raise ValidationError("Date cannot be in the past")
            
from django_currentuser.db.models import CurrentUserField
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = CurrentUserField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # due_date = models.DateField(null=True, blank=True, default=None, validators=[validate_date])
    due_date = models.DateField()
    done = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(choices=PRIO, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["done"]

    

