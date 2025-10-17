from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Only process the image if it exists and is not the default
        if self.image and os.path.exists(self.image.path):
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        