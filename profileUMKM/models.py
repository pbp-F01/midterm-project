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

    foto = models.URLField(blank=True, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png")

    tanggal_pembuatan = models.DateTimeField("Tanggal Pembuatan", auto_now_add=True)