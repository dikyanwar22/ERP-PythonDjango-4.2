from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.db import connection

from erp.models.models import Mahasiswa
from erp.models.forms import MahasiswaForm


# Read (Tampilkan data)
def index(request):
    return render(request, 'modules/warehouse/index.html')

#GET data JSON
def get_module(request):
    if request.method == "GET":
        mahasiswa_list = Mahasiswa.objects.values("id", "nama", "nim", "jurusan")
        mahasiswa_data = list(mahasiswa_list)
        return JsonResponse({"data": mahasiswa_data}, safe=False)
    return JsonResponse({"error": "Invalid request"}, status=400)

#halaman add
def add_data(request):
    return render(request, 'modules/warehouse/add.html')

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

