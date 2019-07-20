from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
# from accounts.models import User
from PIL import *
from PIL import Image


from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()



class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="person")
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    dob_in_dd_mm_yyyy=models.DateField(blank=True,null=True)
    lives_in=models.CharField(max_length=200,null=True,blank=True)
    studies_at=models.CharField(max_length=200,null=True,blank=True)
    profilepic=models.ImageField(upload_to="",null=True,blank=True,default="defaultprofilepic/default_profile.png")
    friend = models.ManyToManyField('self',through="Friends",symmetrical=False)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        image = Image.open(self.profilepic)
        (width, height) = image.size
        size = ( 100, 100)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.profilepic.path)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("person:all")


    class Meta:
        ordering = ["name"]



class Friends(models.Model):
    from_person = models.ForeignKey(Person,on_delete=models.CASCADE, related_name="from_person")
    to_person = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="to_person")

    def __str__(self):
        return self.from_person.user

    class Meta:
        unique_together = ("from_person", "to_person")
        ordering=["to_person"]
