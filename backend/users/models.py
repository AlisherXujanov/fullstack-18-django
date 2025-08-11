from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # id  =>  automatically set when created -- UUID  =>
    # Universally Unique ID
    # 8 4 4 8 8  # ex: qqqqqqqq-qqqq-qqqq-qqqqqqqq
    # ----------------------------------------------------------
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey   =>  one-to-one
    # ManyToMany   
    # ManyToOne    
    # -------------------
    # CASCADE  => automatically delete the child-object
    # SET_NULL => sets to null
    # PREVENT  => prevents the model-object from deletion
    # ----------------------------------------------------------
    bio = models.TextField(max_length=255)
    # image = models.ImageField(default="profile_pics/default.png")

    def __str__(self):
        return f"Profile of {self.user.username}"



# register a new account  =>  django creates a new User
# When the user object is created, we call a signal 
#                                  that creates a Profile for him

