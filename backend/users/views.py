from django.shortcuts import render
from .models import Profile

def home(request):
    context = {
        "my_name": "Alisher",
        "profile": Profile.objects.first()
    }
    return render(request, 'index.html', context)
