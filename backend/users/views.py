from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm

def home(request):
    context = {
        "my_name": "Alisher",
        "profile": Profile.objects.first()
    }
    return render(request, 'index.html', context)


def profile(request, pk=1):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile
    }
    return render(request, 'profile.html', context)

    