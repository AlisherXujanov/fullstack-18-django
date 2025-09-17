from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Posts

# post_save  == event in JS
# receiver   == event listener in JS


@receiver(post_save, sender=Posts)
def print_post(sender, instance, created, **kwargs):
    if created:
        print("="*20)
        print("="*20)
        print("TITLE", instance.title)  
        print("CONTENT", instance.content)
        print("="*20)
        print("="*20)
