from django.urls import path
from .views import *

urlpatterns = [
    path('posts', PostsView.as_view(),  name='get_posts'),
    path('create_post', PostCreateView.as_view(),  name='create_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(),  name='update_post'),
    path('delete_post/<int:pk>', PostDeleteView.as_view(),  name='delete_post'),
]
