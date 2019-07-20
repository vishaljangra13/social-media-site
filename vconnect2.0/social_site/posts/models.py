from django.conf import settings
from django.urls import reverse
from django.db import models
from PIL import *
from PIL import Image


from person.models import  Person

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now=True)
    caption = models.TextField()
    cover=models.ImageField(upload_to='images/',blank=True,null=True)
    like=models.ManyToManyField(User,related_name='likes')

    def __str__(self):
        size=(300,300)
        return self.message

    def save(self, *args, **kwargs):
        if self.cover:
            image = Image.open(self.cover)
            (width, height) = image.size
            size = ( 500, 500)
            image = image.resize(size, Image.ANTIALIAS)
            image.save(self.cover.path)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:all')

    class Meta:
        ordering = ["-created_at"]
