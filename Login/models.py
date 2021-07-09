from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # Making one to one relationship with User model of Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    auth_token = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
