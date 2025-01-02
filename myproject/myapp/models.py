from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can add more fields here if necessary
    pass

class CatPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser here
    cat_name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cat_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cat_name} - {self.pet_name}"
