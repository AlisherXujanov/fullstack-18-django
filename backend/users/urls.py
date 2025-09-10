from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(),  name='home'),
    path('profile/<int:pk>', ProfileDetailsView.as_view(),  name='profile'),
    
    path('plus_counter', plus_counter, name='plus_counter'),
    path('minus_counter', minus_counter, name='minus_counter'),
]



