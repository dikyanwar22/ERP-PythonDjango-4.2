import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password
import json
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

SECRET_KEY = "rahasia_super"

# Middleware untuk cek token
def token_required(func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Token tidak ditemukan'}, status=401)

        token = auth_header.split(' ')[1]

        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user_id = decoded['id']
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Token tidak valid'}, status=401)

        return func(request, *args, **kwargs)
    return wrapper

@csrf_exempt
@token_required
def user_profile(request):
    user_id = request.user_id  # Dapatkan ID dari token

    with connection.cursor() as cursor:
        cursor.execute("SELECT id, username, email FROM auth_user WHERE id=%s", [user_id])
        user = cursor.fetchone()

    if not user:
        return JsonResponse({'error': 'User tidak ditemukan'}, status=404)

    return JsonResponse({'id': user[0], 'username': user[1], 'email': user[2]}, status=200)

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            return JsonResponse({'error': 'Semua field harus diisi'}, status=400)

        hashed_password = make_password(password)

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO auth_user (username, email, password, is_superuser, is_staff, is_active) VALUES (%s, %s, %s, %s, %s, %s)",
                    [username, email, hashed_password, 0, 0, 1]
                )
            return JsonResponse({'message': 'Registrasi berhasil'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Metode tidak diizinkan'}, status=405)
