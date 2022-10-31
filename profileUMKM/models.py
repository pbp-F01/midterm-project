from django.db import models
from landing.models import Profile


class ProfileUMKM(models.Model):
    nama = models.CharField("Nama UMKM", max_length=255)

    pemilik = models.ForeignKey(
        to=Profile, on_delete=models.CASCADE, related_name="lokasi_UMKM"
    )

    no_telepon = models.CharField("Nomor Telepon", max_length=32, unique=True)

    email = models.EmailField("Email Address", unique=True)

    kontak = models.CharField(max_length=32)

    kota = models.CharField(max_length=32)

    provinsi = models.CharField(max_length=32)

    kodepos = models.PositiveIntegerField("Kode Pos")

    foto = models.URLField(blank=True)

    tanggal_pembuatan = models.DateTimeField("Tanggal Pembuatan", auto_now_add=True)
