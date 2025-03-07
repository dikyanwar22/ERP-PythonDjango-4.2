from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    jurusan = models.CharField(max_length=50)

    class Meta:
        db_table = "erp_mahasiswa"  # Ganti sesuai nama tabel yang diinginkan
