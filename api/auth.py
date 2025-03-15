import jwt
import datetime
import json
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

SECRET_KEY = "rahasia_super"

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Cek ke database menggunakan Django database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username, password FROM auth_user WHERE username=%s", [username])
            user = cursor.fetchone()

        if not user or user[2] != password:  # user[2] = password dari database
            return JsonResponse({'error': 'Username atau password salah'}, status=401)

        # Generate JWT Token (Bearer Token)
        payload = {
            'id': user[0],  # user[0] = ID
            'username': user[1],  # user[1] = Username
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expired dalam 1 jam
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return JsonResponse({'token': token}, status=200)

    return JsonResponse({'error': 'Metode tidak diizinkan'}, status=405)
