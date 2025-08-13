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
    context = { "form": PostsForm() }

    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_posts')

    return render(request, "create_post.html", context)


def update_post(request, pk:int):
    post = Posts.objects.get(pk=pk)
    context = {"form": PostsForm(instance=post)}

    if request.method == "POST":
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('get_posts')

    return render(request, "update_post.html", context)


def delete_post(request, pk:int):
    post = Posts.objects.get(pk=pk)
    post.delete()
    return redirect("get_posts")


