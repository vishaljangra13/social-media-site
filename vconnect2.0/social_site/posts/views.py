from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http.response import HttpResponse
from django.http import Http404,JsonResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from braces.views import SelectRelatedMixin
from django.db import IntegrityError
from . import forms
from . import models
from .models import Post
from django.urls import reverse
from django.template.loader import render_to_string

from django.contrib.auth import get_user_model
User = get_user_model()


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('caption','cover')
    model = models.Post

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class CheckPage(generic.TemplateView):
    template_name='posts/check.html'


class PostList(LoginRequiredMixin, generic.ListView):
    model=models.Post

class LikePost(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("posts:all")

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post,pk=self.kwargs.get("pk"))
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)

        else:
            post.like.add(request.user)
        return super().get(request, *args, **kwargs)

class SharePost(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("posts:all")

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post,pk=self.kwargs.get("pk"))
        if(post.cover):
            Post.objects.create(user=request.user,caption=post.caption,cover=post.cover)
        else:
            Post.objects.create(user=request.user,caption=post.caption)

        return super().get(request, *args, **kwargs)
