from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from person.models import Person,Friends
from django.views.generic import TemplateView
from . import models
from braces.views import SelectRelatedMixin

class CreatePerson(LoginRequiredMixin,SelectRelatedMixin, generic.CreateView):
    fields = ("name","profilepic", "description","dob_in_dd_mm_yyyy","lives_in","studies_at")
    model = Person
    select_related = ("user")

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SinglePerson(generic.DetailView):
    model = Person

class ListPerson(generic.ListView):
    model = Person

class CheckPage(TemplateView):
    template_name='person/check.html'

class AddFriend(TemplateView):
    template_name='person/h.html'

class UserPerson(TemplateView):
    template_name='person/user_person.html'

class AddFriend(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("person:all")

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person,slug=self.kwargs.get("slug"))

        try:
            Friends.objects.create(from_person=self.request.user.person,to_person=person)

        except IntegrityError:
            messages.warning(self.request,("Warning, already friend of {}".format(person.name)))

        else:
            messages.success(self.request,"You are now friend of the {} ".format(person.name))

        return super().get(request, *args, **kwargs)


class Unfriend(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("person:all")

    def get(self, request, *args, **kwargs):

        try:

            friend = models.Friends.objects.filter(
                to_person__slug=self.kwargs.get("slug"),
                from_person=self.request.user.person
            ).get()

        except models.Friends.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        else:
            friend.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)

class Unfriend2(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("person:single",kwargs={'slug':self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            friend = models.Friends.objects.filter(
                to_person__slug=self.kwargs.get("slug"),
                from_person=self.request.user.person
            ).get()

        except models.Friends.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        else:
            friend.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)

class AddFriend2(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("person:single",kwargs={'slug':self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person,slug=self.kwargs.get("slug"))

        try:
            Friends.objects.create(from_person=self.request.user.person,to_person=person)

        except IntegrityError:
            messages.warning(self.request,("Warning, already friend of {}".format(person.name)))

        else:
            messages.success(self.request,"You are now friend of the {} ".format(person.name))

        return super().get(request, *args, **kwargs)
