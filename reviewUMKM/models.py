from django.db import models
from profileUMKM.models import ProfileUMKM
from landing.models import Profile


class Review(models.Model):
    author = models.ForeignKey(
        to=Profile, on_delete=models.CASCADE, related_name="reviews"
    )
    review_date = models.DateTimeField(auto_now_add=True)
    rate_choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rating = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=2048)
    umkm = models.ForeignKey(to=ProfileUMKM, on_delete=models.CASCADE)
