from django.shortcuts import render, redirect
from .models import Mahasiswa
from .forms import MahasiswaForm

# Read (Tampilkan data)
def index(request):
    mahasiswa = Mahasiswa.objects.all()
    return render(request, 'index.html', {'mahasiswa': mahasiswa})

# Create (Tambah data)
def tambah_mahasiswa(request):
    if request.method == "POST":
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MahasiswaForm()
    return render(request, 'tambah.html', {'form': form})

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
    return render(request, 'edit.html', {'form': form})

# Delete (Hapus data)
def hapus_mahasiswa(request, id):
    mahasiswa = Mahasiswa.objects.get(id=id)
    mahasiswa.delete()
    return redirect('index')
