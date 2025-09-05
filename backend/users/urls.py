from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(),  name='home'),
    path('profile/<int:pk>', ProfileDetailsView.as_view(),  name='profile'),
]



