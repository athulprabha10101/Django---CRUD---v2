from django.shortcuts import render

# Create your views here.


def user_login(request):
    return render(request, 'user_login.html')

def admin_login(request):
    return render(request, 'admin_login.html')

