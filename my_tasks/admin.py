from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()
