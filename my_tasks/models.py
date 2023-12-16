from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
PRIO = ((0, "Low"), (1, "Medium"), (2, "High"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    due_date = models.DateTimeField()
    done = models.BooleanField(default=False)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(choices=PRIO, default=1)

# The on_delete argument emulates the behaviour of an SQL database when
# an author is deleted. As we have set this to models.CASCADE: if a user
# is deleted, then any posts they have authored will also be deleted.
# If, instead, you wanted to delete each post manually if their author
# was deleted, then you could set this to RESTRICT. It is important
# that on_delete is used as it will ensure database integrity.
# ***Maybe change this to RESTRICT

# The related_name parameter is optional but is useful as it gives
# a meaningful name to the relation from the User model to the Post.
# Without it, Django would autogenerate the name of author_set for a
# query of a user's posts, which is not as semantic as blog_posts.
