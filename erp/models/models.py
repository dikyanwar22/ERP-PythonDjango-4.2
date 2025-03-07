from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    jurusan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama
