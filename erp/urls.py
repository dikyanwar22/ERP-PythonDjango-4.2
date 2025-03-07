from django.urls import path
from .backend.views import index, tambah_mahasiswa, edit_mahasiswa, hapus_mahasiswa, get_module

urlpatterns = [
    path('', index, name='index'),
    path('tambah/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('edit/<int:id>/', edit_mahasiswa, name='edit_mahasiswa'),
    path('hapus/<int:id>/', hapus_mahasiswa, name='hapus_mahasiswa'),
    path('get_module/', get_module, name='get_module'),  # Sesuai dengan views.py
]
