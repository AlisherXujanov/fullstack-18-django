from django.shortcuts import render, redirect
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




def update_counter(request, inc_dec:str, num:int=1):
    current_num = request.session.get('counter', 0)
    match inc_dec:
        case 'inc':
            current_num += num
        case 'dec':
            current_num -= num
        case _:
            raise ValueError(f"Invalid {inc_dec=} case")
    request.session['counter'] = current_num
    return True


def plus_counter(request):
    if not update_counter(request, 'inc'):
        print("Error happened")
    return redirect('home')
    
# in HTML  ->  request.session.counter
def minus_counter(request):
    if not update_counter(request, 'dec'):
        print("Error happened")
    return redirect('home')
