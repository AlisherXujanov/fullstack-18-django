from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm

# CRUD
# - Create
# - Read
# - Update
# - Delete

# Create your views here.
def get_posts(request):
    context = {
        "posts": Posts.objects.all()
    }
    return render(request, "posts.html", context)



def create_post(request):
    context = {
        "form": PostsForm()
    }

    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_posts')

    return render(request, "create_post.html", context)


