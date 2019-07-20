from django.db import models
from django.urls import reverse
# Create your models here.
from posts.models import  Post

from django.contrib.auth import get_user_model
User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comments")
    add_comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("comment:create")

    def __str__(self):
        return self.text
