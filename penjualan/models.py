from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Laporan(models.Model):
        nama_umkm = models.CharField(max_length=150, null=True)
        date = models.DateField()
        jumlah_terjual = models.IntegerField()
        revenue = models.IntegerField()
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)