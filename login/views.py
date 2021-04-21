from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.sessions.models import Session
from django.contrib import messages
from .filters import *
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
# Create your views here.

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def admin_login(request):

    username = 'anfusanu'
    password = 'anfusanu123'
    if request.session.has_key('is_logged'):
        return redirect('user_details')
    elif request.method == 'POST':
        uname = request.POST["username"]
        pword = request.POST["password"]

        if username != uname or password != pword:
            return redirect('admin_login')
        else:
            request.session['is_logged'] = True
            return redirect('user_details')
        
    return render(request,'admin_login.html')
    
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def user_details(request):
    if request.session.has_key('is_logged'):
        user_filter = UserFilter(request.GET, queryset=User.objects.all())
        
        user = User.objects.all()
        user =User.objects.exclude(is_superuser=1)
        return render(request,'user_details.html',{'user' : user,'user_filter' : user_filter})
    else:
        return redirect('admin_login')


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        email = request.POST['email']
        # if username or password1 or email is None:
        #     messages.info(request,'Please full fill the form')
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Taken")
        else:
            user = User.objects.create_user(username=username,password=password1,email=email)    
            user.save()
            return redirect('user_details')
    return render(request,'add_user.html')


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def admin_logout(request):
    del request.session['is_logged']
    return redirect('admin_login')


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def delete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('user_details')


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def update(request,pk):
    if request.session.has_key('is_logged'):

        user = User.objects.get(id=pk)
        if request.method == 'POST':
            uname = request.POST['username']
            email = request.POST['email']
            user.username = uname
            user.email = email

            user.save()
            print('success')
            return redirect('user_details')
        print('not success')
    return render(request,'update_user.html',{'user' : user})

# def new(request):
#     if request.session.has_key('is_logged'):
#         user = User.objects.all()
#         user =User.objects.exclude(is_superuser=1)
#         return render(request,'ta`ble.html',{'user' : user})
#     else:
#         return redirect('admin_login')
    