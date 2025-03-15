from django.urls import path
from django.shortcuts import redirect
from .backend import views, auth, profile, modul, helpdesk

def auth_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('/erp/login/')  # Jika tidak ada session, arahkan ke login
        return view_func(request, *args, **kwargs)
    return wrapper

#untuk pertama kali arahkan url kesini
# http://127.0.0.1:8000/erp/

urlpatterns = [
    path('', auth_required(views.index), name='index'),
    path('add_data/', auth_required(views.add_data), name='add_data'),
    path('get_module/', auth_required(views.get_module), name='get_module'),
    path('add_action/', auth_required(views.add_action), name='add_action'),
    path('edit/<int:id>/', auth_required(views.function_edit), name='edit_mahasiswa'),
    path('view_edit/', auth_required(views.function_view_edit), name='view_edit'),
    path('aksi_edit/', auth_required(views.function_edit_action), name='edit_action'),
    path('hapus/<int:id>/', auth_required(views.hapus_mahasiswa), name='hapus_mahasiswa'),
    path('profile/', auth_required(profile.profile), name='profile'),
    path('modul/', auth_required(modul.module_user), name='module_user'),
    path('helpdesk/', auth_required(helpdesk.helpdesk_in), name='notif_helpdesk'),

    # Khusus untuk modul
    path('modules/', auth_required(modul.modul), name='custom_modules'),
    path('menu/', auth_required(modul.menu), name='custom_menu'),
    path('sub_menu/', auth_required(modul.sub_menu), name='custom_sub_menu'),
    
    # Login, Register, Logout
    path('login/', auth.login, name='login'),
    path('login_action/', auth.login_action, name='login_action'),
    path('register/', auth.register, name='register'),
    path('register_action/', auth.register_action, name='register_action'),
    path('logout/', auth.logout_action, name='logout_action'),
]