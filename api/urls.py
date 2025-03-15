from django.urls import path
from . import auth, views

urlpatterns = [
    path('login/', auth.login_user, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('register/', views.register_user, name='api_register'),
]

# contoh url :
# http://127.0.0.1:8000/api/register/
# method : post > form-data