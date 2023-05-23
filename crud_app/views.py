from django.shortcuts import render, redirect
from .models import custom_user
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache


# Create your views here.

@never_cache
def user_login(request):
    if 'username' in request.session:
        username = request.session['username']
        user = custom_user.objects.get(username = username)

        if not user.is_superuser:
            return redirect('userhome')
        else:
            return redirect('adminhome')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = custom_user.objects.get(username = username, password = password)
            
            if user is not None:
                if not user.is_superuser:    
                    request.session['username'] = username
                    return redirect('userhome')
                else:
                    return render(request, 'user_login.html', {'user404': 'Please use admin login'})
            
        except custom_user.DoesNotExist:
            return render(request, 'user_login.html', {'user404': 'Wrong credentials'})

    return render(request, 'user_login.html')

@never_cache
def admin_login(request):
    if 'username' in request.session:
        username = request.session['username']
        user = custom_user.objects.get(username = username)

        if user.is_superuser:
            return redirect('adminhome')
        else:
            return redirect('userhome')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = custom_user.objects.get(username = username, password = password)
            
            if user is not None:
                if user.is_superuser:    
                    request.session['username'] = username
                    return redirect('adminhome')
                else:
                    return render(request, 'admin_login.html', {'admin404': 'Please use user login'})
            
        except custom_user.DoesNotExist:
            return render(request, 'admin_login.html', {'admin404': 'Wrong credentials'})

    return render(request, 'admin_login.html')


@never_cache
def user_home(request):
    if 'username' in request.session: 
        username =request.session['username']
        user = custom_user.objects.get(username=username)
        
        if not user.is_superuser:
            return render (request, 'user_home.html')
        else: return redirect('adminhome')
    
    return redirect('userlogin')
    

@never_cache
def admin_home(request):
    
    if 'username' in request.session: 
        username = request.session['username']
        user = custom_user.objects.get(username=username)
    
        if user.is_superuser:
            
            search = request.POST.get('search')

            if search:
                details = custom_user.objects.filter(username__istartswith = search)
            else:
                details = custom_user.objects.filter(is_superuser = False)
            return render(request, 'admin_home.html', {'detailskey':details})
    
    return redirect('userlogin')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if custom_user.objects.filter(username = username).exists():
                return render(request, 'signup.html',{'taken':'Username taken'})
            if custom_user.objects.filter(email = email):
                return render(request, 'signup.html',{'taken': 'Email already registered'})
            else:
                custom_user(first_name = name, username = username, password = password, email = email).save()
                return render(request, 'signup.html',{'pw_error':'Success !!'})
        else:
            return render(request, 'signup.html',{'pw_error':'Password mismatch'})
    return render(request, 'signup.html') 

def logout(request):
    if 'username' in request.session:
        request.session.flush()
        return redirect('userlogin')
    
def add_user(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword: 
            if custom_user.objects.filter(username = username).exists():
                return render(request, 'add_user.html',{'pw_error': 'Username taken'})
            if custom_user.objects.filter(email = email):
                return render(request, 'add_user.html',{'pw_error': 'Email already registered'})
            else:
                custom_user(first_name = name, username = username, email = email, password = password).save()
                return redirect('adminhome')
        else:
            return render(request, 'add_user.html',{'pw_error': 'Password mismatch'}) 
    return render(request, 'add_user.html')

def edit_details(request, id):
    if 'username' in request.session:
        user = custom_user.objects.get(id = id)
        return render(request, 'edit_details.html', {'user': user})

def update_details(request, id):
    user = custom_user.objects.get(id = id)
    
    if request.method == 'POST':
        user.first_name = request.POST.get('name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('adminhome')
    
    return render(request, 'edit_details.html', {'user': user})

def delete_user(request, id):
    user = custom_user.objects.get(id = id)
    user.delete()
    return redirect('adminhome')