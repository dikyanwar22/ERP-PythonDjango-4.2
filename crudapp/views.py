from django.shortcuts import render, redirect
from django.db import connection

from .models import Mahasiswa
from .forms import MahasiswaForm

# Read (Tampilkan data)
# def index(request):
#     mahasiswa = Mahasiswa.objects.all()
#     return render(request, 'index.html', {'mahasiswa': mahasiswa})

#atau bisa juga pakai cara ini
def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, nama, nim, jurusan FROM crudapp_mahasiswa")  # Sesuaikan dengan tabel Anda
        mahasiswa = cursor.fetchall()  # Ambil semua hasil query

    # Mengonversi hasil query ke dalam daftar dictionary
    mahasiswa_list = []
    for row in mahasiswa:
        mahasiswa_list.append({
            'id': row[0],
            'nama': row[1],
            'nim': row[2],
            'jurusan': row[3]
        })

    return render(request, 'modules/crud/index.html', {'mahasiswa': mahasiswa_list})

# Create (Tambah data)
def tambah_mahasiswa(request):
    if request.method == "POST":
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MahasiswaForm()
    return render(request, 'modules/crud/tambah.html', {'form': form})

# Update (Edit data)
def edit_mahasiswa(request, id):
    mahasiswa = Mahasiswa.objects.get(id=id)
    if request.method == "POST":
        form = MahasiswaForm(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MahasiswaForm(instance=mahasiswa)
    return render(request, 'modules/crud/edit.html', {'form': form})

# Delete (Hapus data)
def hapus_mahasiswa(request, id):
    mahasiswa = Mahasiswa.objects.get(id=id)
    mahasiswa.delete()
    return redirect('index')
