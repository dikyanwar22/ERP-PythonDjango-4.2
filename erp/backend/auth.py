from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


# login
def login(request):
    return render(request, 'modules/login.html')

#login action
def login_action(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Cek apakah email ada di database
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username, password, first_name, last_name FROM auth_user WHERE email = %s AND is_active = 1", [email])
            user = cursor.fetchone()

        if user:
            user_id, username, hashed_password, first_name, last_name = user
            
            # Cek password yang dimasukkan dengan hash di database
            if check_password(password, hashed_password):
                # Set session untuk login
                request.session['user_id'] = user_id
                request.session['username'] = username
                request.session['first_name'] = first_name
                request.session['last_name'] = last_name
                request.session['email'] = email

                messages.success(request, "Login berhasil!")
                return redirect('index')  # Redirect ke halaman utama

            else:
                messages.error(request, "Password salah!")
        else:
            messages.error(request, "Email tidak ditemukan atau akun tidak aktif!")

    return render(request, 'modules/login.html')


# register
def register(request):
    return render(request, 'modules/register.html')

# register action
def register_action(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validasi password cocok
        if password != password2:
            messages.error(request, "Password dan konfirmasi password tidak cocok.")
            return redirect('register_action')

        # Cek apakah username sudah ada
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM auth_user WHERE username = %s", [username])
            if cursor.fetchone():
                messages.error(request, "Username sudah digunakan.")
                return redirect('register_action')

        # Cek apakah email sudah ada
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM auth_user WHERE email = %s", [email])
            if cursor.fetchone():
                messages.error(request, "Email sudah terdaftar.")
                return redirect('register_action')

        # Hash password sebelum disimpan
        hashed_password = make_password(password)

        # Simpan user ke database menggunakan query MySQL langsung
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO auth_user (first_name, last_name, email, username, password, is_active, is_superuser, is_staff, date_joined)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """, [first_name, last_name, email, username, hashed_password, 1, 0, 0])

        messages.success(request, "Pendaftaran berhasil! Silakan login.")
        return redirect('login')  # Ganti dengan URL login

    return render(request, 'modules/register.html')

#logout
def logout_action(request):
    request.session.flush()  # Hapus semua session
    messages.success(request, "Logout berhasil!")
    return redirect('login_action')  # Redirect ke halaman login
