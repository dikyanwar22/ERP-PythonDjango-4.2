from django.urls import path
from .backend.views import index, tambah_mahasiswa, edit_mahasiswa, hapus_mahasiswa, add_data, get_module, add_action

urlpatterns = [
    path('', index, name='index'),
    path('tambah/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('edit/<int:id>/', edit_mahasiswa, name='edit_mahasiswa'),
    path('hapus/<int:id>/', hapus_mahasiswa, name='hapus_mahasiswa'),

    path('add_data/', add_data, name='add_data'),
    path('get_module/', get_module, name='get_module'),
    path('add_action/', add_action, name='add_action'),
]

