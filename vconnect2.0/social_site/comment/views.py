from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http.response import HttpResponse
from django.http import Http404,JsonResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from braces.views import SelectRelatedMixin
from . import models
from . models import Post
from django.urls import reverse
from django.template.loader import render_to_string
from comment.models import Comment

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
from comment.forms import CommentForm
class SinglePost(generic.DetailView):

    model=Post



@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('comment:single', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment/comment_form.html', {'form': form})
