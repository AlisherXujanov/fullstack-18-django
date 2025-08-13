from django.shortcuts import render
from .models import Posts

# Create your views here.
def get_posts(request):
    context = {
        "posts": Posts.objects.all()
    }
    return render(request, "posts.html", context)