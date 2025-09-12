from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# post_save  == event in JS
# receiver   == event listener in JS

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """This function will be called every time a new user is created."""
    if created:
        Profile.objects.create(user=instance)



