from django.urls import path
from .backend.views import index, tambah_mahasiswa, function_edit, function_view_edit, hapus_mahasiswa, add_data, get_module, add_action

urlpatterns = [
    path('', index, name='index'),
    path('tambah/', tambah_mahasiswa, name='tambah_mahasiswa'),
    

    path('add_data', add_data, name='add_data'),
    path('get_module/', get_module, name='get_module'),
    path('add_action', add_action, name='add_action'),
    path('edit/<int:id>', function_edit, name='edit_mahasiswa'),
    path('view_edit/', function_view_edit, name='view_edit'),

    path('hapus/<int:id>', hapus_mahasiswa, name='hapus_mahasiswa'),
]

