from django.shortcuts import redirect

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Cek apakah user mengakses halaman index tanpa login
        if request.path == '/' and 'user_id' not in request.session:
            return redirect('login')  # Redirect ke halaman login

        return self.get_response(request)
