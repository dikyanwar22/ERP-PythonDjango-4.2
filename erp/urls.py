from django.urls import path
from django.shortcuts import redirect
from .backend.views import index, function_edit, function_view_edit, function_edit_action, hapus_mahasiswa, add_data, get_module, add_action
from .backend.auth import login, login_action, register, register_action, logout_action
from .backend.profile import profile
from .backend.modul import module_user, modul, menu, sub_menu
from .backend.helpdesk import helpdesk_in

# Wrapper function untuk memeriksa session
def auth_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('login')  # Redirect ke halaman login
        return view_func(request, *args, **kwargs)
    return wrapper

urlpatterns = [
    path('', auth_required(index), name='index'), # Gunakan wrapper di sini agar yang sudah login

    path('add_data/', auth_required(add_data), name='add_data'),
    path('get_module/', auth_required(get_module), name='get_module'),
    path('add_action/', auth_required(add_action), name='add_action'),
    path('edit/<int:id>/', auth_required(function_edit), name='edit_mahasiswa'),
    path('view_edit/', auth_required(function_view_edit), name='view_edit'),
    path('aksi_edit/', auth_required(function_edit_action), name='edit_action'),
    path('hapus/<int:id>/', auth_required(hapus_mahasiswa), name='hapus_mahasiswa'),

    path('profile/', auth_required(profile), name='profile'),

    path('modul/', auth_required(module_user), name='module_user'),
    path('helpdesk/', auth_required(helpdesk_in), name='notif_helpdesk'),

    #khusus untuk modul
    path('modules/', auth_required(modul), name='custom_modules'),
    path('menu/', auth_required(menu), name='custom_menu'),
    path('sub_menu/', auth_required(sub_menu), name='custom_sub_menu'),
    #khusus untuk modul

    path('login/', login, name='login'),
    path('login_action/', login_action, name='login_action'),

    path('register/', register, name='register'),
    path('register_action/', register_action, name='register_action'),

    path('logout/', logout_action, name='logout_action'),

]

