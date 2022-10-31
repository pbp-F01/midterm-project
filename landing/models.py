from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    roles = models.CharField(max_length=1)

    def konsumen(self):
        if self.roles == 'K':
            return True
        return False

    def investor(self):
        if self.roles == 'I':
            return True
        return False
    
    def pemilik(self):
        if self.roles == 'P':
            return True
        return False
        
    def __str__(self):
        return self.user.username

    def natural_key(self):
        return self.name 