from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# CRUD
# - Create
# - Read
# - Update
# - Delete


class PostsView(ListView):
    model = Posts
    template_name = "posts.html"
    context_object_name = "posts"  # defaults to "object_list"



# @login_required
# def create_post(request):
#     context = { "form": PostsForm() }

#     if request.method == "POST":
#         form = PostsForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.author = request.user
#             obj.save()
#             return redirect('get_posts')

#     return render(request, "create_post.html", context)


class PostCreateView(CreateView):
    model = Posts
    form_class = PostsForm  # This lets to use the form that we created inside templates
    template_name = 'create_post.html'
    success_url = '/posts'

    # set request.user as an author of the post
    def form_valid(self, post):
        post.instance.author = self.request.user
        return super().form_valid(post)


# @login_required
# def update_post(request, pk: int):
#     post = Posts.objects.get(pk=pk, author=request.user)
#     context = {"form": PostsForm(instance=post)}

#     if request.method == "POST":
#         form = PostsForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('get_posts')

#     return render(request, "update_post.html", context)


class UpdatePostView(UpdateView):
    model = Posts
    template_name = 'update_post.html'
    success_url = '/posts'
    form_class = PostsForm

# @login_required
# def delete_post(request, pk: int):
#     post = Posts.objects.get(pk=pk, author=request.user)
#     post.delete()
#     return redirect("get_posts")

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'post_confirm_delete.html'
    success_url = '/posts'
