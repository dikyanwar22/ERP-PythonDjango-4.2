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

# Update (Edit data)
def function_edit(request, id):
    return render(request, 'modules/warehouse/edit.html')

#view edit
# def function_view_edit(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)  # Ambil JSON dari request body
#             id = data.get("id")  # Ambil ID dari JSON

#             mahasiswa = Mahasiswa.objects.get(id=id)

#             return JsonResponse({
#                 "nama": mahasiswa.nama,
#                 "nim": mahasiswa.nim,
#                 "jurusan": mahasiswa.jurusan,
#                 "email": mahasiswa.email
#             })
#         except Mahasiswa.DoesNotExist:
#             return JsonResponse({"error": "Mahasiswa tidak ditemukan"}, status=404)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Format JSON salah"}, status=400)

#     return JsonResponse({"error": "Invalid request"}, status=400)

#atau bisa juga dengan cara ini
def function_view_edit(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Ambil JSON dari request body
            id = data.get("id")  # Ambil ID dari JSON

            with connection.cursor() as cursor:
                cursor.execute("SELECT nama, nim, jurusan, email FROM erp_mahasiswa WHERE id = %s", [id])
                row = cursor.fetchone()  # Ambil satu baris hasil query

            if row:
                # Mapping hasil query ke dictionary
                mahasiswa = {
                    "nama": row[0],
                    "nim": row[1],
                    "jurusan": row[2],
                    "email": row[3],
                }
                return JsonResponse(mahasiswa)
            else:
                return JsonResponse({"error": "Mahasiswa tidak ditemukan"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Format JSON salah"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Terjadi kesalahan: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

#aksi untuk mengedit data
# def function_edit_action(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)  # Parsing JSON dari request
            
#             # Ambil mahasiswa berdasarkan ID
#             try:
#                 mahasiswa = Mahasiswa.objects.get(id=data.get("id"))
#             except Mahasiswa.DoesNotExist:
#                 return JsonResponse({"success": False, "message": "Mahasiswa tidak ditemukan"}, status=404)

#             # Update data menggunakan Django Form
#             form = MahasiswaForm(data, instance=mahasiswa)

#             if form.is_valid():
#                 form.save()  # Simpan perubahan
#                 return JsonResponse({"success": True, "message": "Data berhasil diperbarui!"})
            
#             return JsonResponse({"success": False, "message": "Validasi gagal", "errors": form.errors}, status=400)

#         except json.JSONDecodeError:
#             return JsonResponse({"success": False, "message": "Format JSON salah"}, status=400)
#         except Exception as e:
#             return JsonResponse({"success": False, "message": f"Terjadi kesalahan: {str(e)}"}, status=500)

#     return JsonResponse({"success": False, "message": "Invalid request"}, status=400)

#atau bisa juga dengan cara ini
def function_edit_action(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Ambil JSON dari request body
            id = data.get("id")
            nama = data.get("nama")
            nim = data.get("nim")
            email = data.get("email")
            jurusan = data.get("jurusan")

            if not all([id, nama, nim, email, jurusan]):  # Pastikan tidak ada data kosong
                return JsonResponse({"error": "Semua field harus diisi"}, status=400)

            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE erp_mahasiswa 
                    SET nama = %s, nim = %s, email = %s, jurusan = %s 
                    WHERE id = %s
                """, [nama, nim, email, jurusan, id])

            return JsonResponse({"message": "Data berhasil diperbarui!"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Format JSON salah"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Terjadi kesalahan: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

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


