from statistics import mode
from django.db import models

# Create your models here.
class Laporan(models.Model):
        nama_umkm = models.CharField(max_length=150, null=True)
        date = models.DateField()
        jumlah_terjual = models.IntegerField()
        revenue = models.IntegerField()