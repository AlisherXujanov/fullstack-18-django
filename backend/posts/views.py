from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# CRUD
# - Create
# - Read
# - Update
# - Delete


class PostsView(ListView):
    model = Posts
    template_name = "posts.html"
    context_object_name = "posts"  # defaults to "object_list"



@login_required
def create_post(request):
    context = { "form": PostsForm() }

    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('get_posts')

    return render(request, "create_post.html", context)


@login_required
def update_post(request, pk: int):
    post = Posts.objects.get(pk=pk, author=request.user)
    context = {"form": PostsForm(instance=post)}

    if request.method == "POST":
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('get_posts')

    return render(request, "update_post.html", context)


@login_required
def delete_post(request, pk: int):
    post = Posts.objects.get(pk=pk, author=request.user)
    post.delete()
    return redirect("get_posts")


