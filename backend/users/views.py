from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm

from django.views.generic import TemplateView, DetailView


class HomePageView(TemplateView):
    template_name = "index.html"
    

class ProfileDetailsView(DetailView):
    model = Profile
    template_name = "profile.html"
    context_object_name = "profile"  # defaults to "object"

    def get_queryset(self):
        return Profile.objects.filter(id=self.kwargs['pk'])



def plus_counter(request, num):
    # request.session['counter']
    ...

# in HTML  ->  request.session.counter


def minus_counter(request, num):
    # request.session['counter']
    ...