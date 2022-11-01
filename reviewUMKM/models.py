from django.db import models
from django.utils import timezone
from profileUMKM.models import ProfileUMKM

# Create your models here.

class Review(models.Model):
    author = models.CharField(max_length=40, default="anonymous")
    review_date = models.DateTimeField(default=timezone.now)
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=4000)
    umkm = models.ForeignKey(ProfileUMKM, on_delete=models.CASCADE)

    def __str__(self):
        return self.umkm.title
    
    

