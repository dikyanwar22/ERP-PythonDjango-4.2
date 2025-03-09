from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
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

# Proses insert data (API)
# def add_action(request):
#     if request.method == "POST":
#         data = json.loads(request.body)  # Parsing JSON dari request
#         form = MahasiswaForm(data)
        
#         if form.is_valid():
#             mahasiswa = form.save()
#             return JsonResponse({"success": True, "message": "Data berhasil ditambahkan!", "id": mahasiswa.id})
        
#         return JsonResponse({"success": False, "message": "Validasi gagal", "errors": form.errors}, status=400)

#     return JsonResponse({"error": "Invalid request"}, status=400)

#atau bisa juga dengan cara ini menggunakan mysql
import json
from django.http import JsonResponse
from django.db import connection  # Koneksi ke database

def add_action(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parsing JSON dari request
            nama = data.get("nama")
            nim = data.get("nim")
            email = data.get("email")
            jurusan = data.get("jurusan")

            # Validasi data tidak boleh kosong
            if not nama or not nim or not email or not jurusan:
                return JsonResponse({"success": False, "message": "Semua field harus diisi!"}, status=400)

            # Query insert ke MySQL
            with connection.cursor() as cursor:
                sql = "INSERT INTO erp_mahasiswa (nama, nim, email, jurusan) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, [nama, nim, email, jurusan])
                connection.commit()  # Simpan perubahan

            return JsonResponse({"success": True, "message": "Data berhasil ditambahkan!"})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Format JSON tidak valid"}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "message": "Terjadi kesalahan: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

# Delete (Hapus data)
# def hapus_mahasiswa(request, id):
#     mahasiswa = Mahasiswa.objects.get(id=id)
#     mahasiswa.delete()
#     return redirect('index')   

#atau bisa juga dengan cara ini
def hapus_mahasiswa(request, id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM erp_mahasiswa WHERE id = %s", [id])
    return redirect('index') 








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



