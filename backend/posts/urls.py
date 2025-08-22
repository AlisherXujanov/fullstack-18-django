from django.urls import path
from .views import *

urlpatterns = [
    path('posts', get_posts,  name='get_posts'),
    path('create_post', create_post,  name='create_post'),
    path('update_post/<int:pk>', update_post,  name='update_post'),
    path('delete_post/<int:pk>', delete_post,  name='delete_post'),
]
